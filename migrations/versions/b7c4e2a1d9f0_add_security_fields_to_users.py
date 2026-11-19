"""Add MFA and security session fields to users

Revision ID: b7c4e2a1d9f0
Revises: a3e1c5d7b9f2
Create Date: 2026-11-20
"""

import sqlalchemy as sa
from alembic import op


revision = "b7c4e2a1d9f0"
down_revision = "a3e1c5d7b9f2"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column("mfa_enabled", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column("users", sa.Column("mfa_secret_encrypted", sa.Text(), nullable=True))
    op.add_column("users", sa.Column("mfa_recovery_codes", sa.JSON(), nullable=True))
    op.add_column("users", sa.Column("admin_permissions", sa.JSON(), nullable=True))
    op.add_column(
        "users",
        sa.Column("security_version", sa.Integer(), nullable=False, server_default="1"),
    )

    # Existing administrators must enroll MFA before admin access is granted.
    op.execute(sa.text("UPDATE users SET mfa_enabled = false WHERE type = 'admin'"))


def downgrade():
    op.drop_column("users", "security_version")
    op.drop_column("users", "admin_permissions")
    op.drop_column("users", "mfa_recovery_codes")
    op.drop_column("users", "mfa_secret_encrypted")
    op.drop_column("users", "mfa_enabled")
