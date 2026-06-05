"""create system_settings table

Revision ID: 5dac63588faa
Revises: 4547b010ca1c
Create Date: 2026-06-04 22:35:54.733534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dac63588faa'
down_revision: Union[str, None] = '4547b010ca1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "system_settings",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    # Seed default show_gemini_omni value
    op.execute(
        "INSERT INTO system_settings (id, value, description) VALUES "
        "('show_gemini_omni', 'false', 'Enable Gemini Omni model visibility')"
    )


def downgrade() -> None:
    op.drop_table("system_settings")

