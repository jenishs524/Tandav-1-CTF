#!/usr/bin/env python3
import argparse
import os
import sys

from Tandav import create_app
from Tandav.models import Teams, Users, db
from Tandav.utils.crypto import pii_search_index


def main():
    parser = argparse.ArgumentParser(description="Encrypt Tandav PII on a staging database")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-size", type=int, default=100)
    args = parser.parse_args()

    if not os.getenv("PII_ENCRYPTION_KEY"):
        print("PII_ENCRYPTION_KEY is required", file=sys.stderr)
        return 2
    if not os.getenv("PII_SEARCH_KEY"):
        print("PII_SEARCH_KEY is required", file=sys.stderr)
        return 2
    if os.getenv("ALLOW_PII_MIGRATION") != "1":
        print("Set ALLOW_PII_MIGRATION=1 only after an encrypted backup and restore test", file=sys.stderr)
        return 2

    app = create_app()
    migrated_users = 0
    migrated_teams = 0
    with app.app_context():
        for model, fields in ((Users, ("website", "affiliation", "country")), (Teams, ("website", "affiliation", "country"))):
            offset = 0
            while True:
                rows = model.query.order_by(model.id).offset(offset).limit(args.batch_size).all()
                if not rows:
                    break
                for row in rows:
                    for field in fields:
                        value = getattr(row, field)
                        if value is not None and not (
                            isinstance(value, str) and value.startswith("v1:")
                        ):
                            if not args.dry_run:
                                model.query.filter_by(id=row.id).update(
                                    {field: value}, synchronize_session=False
                                )
                    if getattr(row, "email", None):
                        if not args.dry_run:
                            model.query.filter_by(id=row.id).update(
                                {"email_hmac": pii_search_index(row.email)},
                                synchronize_session=False,
                            )
                    if isinstance(row, Users):
                        migrated_users += 1
                    else:
                        migrated_teams += 1
                if not args.dry_run:
                    db.session.commit()
                offset += args.batch_size
    print("PII migration staged")
    print("User records considered: {}".format(migrated_users))
    print("Team records considered: {}".format(migrated_teams))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
