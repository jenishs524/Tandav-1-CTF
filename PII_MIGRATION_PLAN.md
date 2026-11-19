# PII Migration Plan

## Required preconditions

1. Stop writes or place the staging application in maintenance mode.
2. Create and verify an encrypted database backup.
3. Restore the backup into a separate database and verify record counts.
4. Set `PII_ENCRYPTION_KEY` and `PII_SEARCH_KEY` in staging secrets.
5. Set `ALLOW_PII_MIGRATION=1` only after restore verification.

## Upgrade

1. Deploy application code.
2. Run `flask db upgrade` in staging.
3. Run:

```text
python scripts/migrate_pii.py --dry-run
ALLOW_PII_MIGRATION=1 python scripts/migrate_pii.py
```

4. Verify:
   - Row counts unchanged.
   - New profile values decrypt.
   - Raw database values for website, affiliation, and country start with `v1:` except legacy values intentionally missed.
   - Email HMAC values are set.
   - Invalid-key reads fail.

## Rollback

- Application rollback does not decrypt data.
- Before migration, retain the verified backup.
- To roll back the application, restore the encrypted backup and downgrade only in the documented maintenance window.
- Never downgrade and then restart an application that may write legacy plaintext without a reviewed plan.

## Script behavior

`scripts/migrate_pii.py`:
- Uses batches.
- Never prints PII or keys.
- Encrypts profile PII through SQLAlchemy bind types.
- Writes normalized email HMAC values.
- Does not delete or replace records.

It has not been executed against production and must not be.
