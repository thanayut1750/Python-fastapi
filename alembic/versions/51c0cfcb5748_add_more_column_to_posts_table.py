"""add more column to posts table

Revision ID: 51c0cfcb5748
Revises: 87796be160df
Create Date: 2022-03-25 17:12:22.336763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51c0cfcb5748'
down_revision = '87796be160df'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
