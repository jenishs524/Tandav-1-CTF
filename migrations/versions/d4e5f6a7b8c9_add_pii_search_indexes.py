"""Add keyed email indexes for PII search compatibility

Revision ID: d4e5f6a7b8c9
Revises: c3d4e5f6a7b8
Create Date: 2026-11-20
"""

import sqlalchemy as sa
from alembic import op


revision = "d4e5f6a7b8c9"
down_revision = "c3d4e5f6a7b8"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("email_hmac", sa.String(length=64), nullable=True))
    op.create_unique_constraint("uq_users_email_hmac", "users", ["email_hmac"])
    op.add_column("teams", sa.Column("email_hmac", sa.String(length=64), nullable=True))
    op.create_unique_constraint("uq_teams_email_hmac", "teams", ["email_hmac"])


def downgrade():
    op.drop_constraint("uq_teams_email_hmac", "teams", type_="unique")
    op.drop_column("teams", "email_hmac")
    op.drop_constraint("uq_users_email_hmac", "users", type_="unique")
    op.drop_column("users", "email_hmac")
