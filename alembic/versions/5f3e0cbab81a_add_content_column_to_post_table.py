"""add content column to post table

Revision ID: 5f3e0cbab81a
Revises: d92a5ca5f7c2
Create Date: 2023-09-02 12:22:01.434411

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5f3e0cbab81a"
down_revision: Union[str, None] = "d92a5ca5f7c2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("content", sa.String, nullable=False),
    )
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
