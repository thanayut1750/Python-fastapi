"""add content column to  post table

Revision ID: c17a5b124760
Revises: d1f3dc727176
Create Date: 2022-03-25 16:52:32.185832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c17a5b124760'
down_revision = 'd1f3dc727176'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
