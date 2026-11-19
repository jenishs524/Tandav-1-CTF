"""Add security audit table and reversible submission backup

Revision ID: c3d4e5f6a7b8
Revises: b7c4e2a1d9f0
Create Date: 2026-11-20
"""

import sqlalchemy as sa
from alembic import op


revision = "c3d4e5f6a7b8"
down_revision = "b7c4e2a1d9f0"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "security_audit_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("actor_user_id", sa.Integer(), nullable=True),
        sa.Column("action", sa.String(length=128), nullable=False),
        sa.Column("target_type", sa.String(length=64), nullable=True),
        sa.Column("target_id", sa.String(length=128), nullable=True),
        sa.Column("ip", sa.String(length=46), nullable=True),
        sa.Column("outcome", sa.String(length=32), nullable=False, server_default="success"),
        sa.Column("metadata_json", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(["actor_user_id"], ["users.id"], ondelete="SET NULL"),
    )
    op.create_table(
        "submission_cleanup_audit",
        sa.Column("submission_id", sa.Integer(), primary_key=True),
        sa.Column("cleaned", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("cleanup_date", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["submission_id"], ["submissions.id"], ondelete="CASCADE"),
    )
    bind = op.get_bind()
    rows = bind.execute(
        sa.text("SELECT id FROM submissions WHERE provided IS NOT NULL")
    ).fetchall()
    cleanup = sa.table(
        "submission_cleanup_audit",
        sa.column("submission_id", sa.Integer()),
        sa.column("cleaned", sa.Boolean()),
        sa.column("cleanup_date", sa.DateTime()),
    )
    now = sa.func.now()
    for (submission_id,) in rows:
        bind.execute(cleanup.insert().values(submission_id=submission_id, cleaned=True, cleanup_date=now))
    bind.execute(sa.text("UPDATE submissions SET provided = NULL"))


def downgrade():
    op.drop_table("submission_cleanup_audit")
    op.drop_table("security_audit_events")
