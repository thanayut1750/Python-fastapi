"""add user table

Revision ID: c3f9a37947fb
Revises: c17a5b124760
Create Date: 2022-03-25 16:56:59.128571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3f9a37947fb'
down_revision = 'c17a5b124760'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False), 
                    sa.Column('email', sa.String(), nullable=False), 
                    sa.Column('password', sa.String(), nullable=False), 
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('user')
    pass
