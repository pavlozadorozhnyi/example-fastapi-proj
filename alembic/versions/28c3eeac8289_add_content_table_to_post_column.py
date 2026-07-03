"""add content table to post column

Revision ID: 28c3eeac8289
Revises: f9292dca12e0
Create Date: 2026-07-02 20:38:52.118564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28c3eeac8289'
down_revision: Union[str, Sequence[str], None] = 'f9292dca12e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", 'content')
    pass
