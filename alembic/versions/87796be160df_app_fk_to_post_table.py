"""app fk to post table

Revision ID: 87796be160df
Revises: c3f9a37947fb
Create Date: 2022-03-25 17:05:10.156970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87796be160df'
down_revision = 'c3f9a37947fb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column('posts','owner_id')
    pass
