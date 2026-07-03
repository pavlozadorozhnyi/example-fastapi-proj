"""add last few columns to posts table

Revision ID: 83cbd479e16b
Revises: 0f0076fb109f
Create Date: 2026-07-02 20:58:02.077272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83cbd479e16b'
down_revision: Union[str, Sequence[str], None] = '0f0076fb109f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(), 
            nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at', 
            sa.TIMESTAMP(timezone=True), nullable = False, server_default=sa.text('NOW()')),)
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
