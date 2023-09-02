"""add last few columns to post table

Revision ID: 3a4dcde37cc4
Revises: fb1e0007bf87
Create Date: 2023-09-02 13:10:55.664926

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3a4dcde37cc4"
down_revision: Union[str, None] = "fb1e0007bf87"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "published",
            sa.Boolean(),
            nullable=False,
            server_default="TRUE",
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
