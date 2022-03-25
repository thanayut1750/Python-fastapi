"""add phone number

Revision ID: f598678d263e
Revises: 656890e0a511
Create Date: 2022-03-25 17:25:57.434362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f598678d263e'
down_revision = '656890e0a511'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user',sa.Column('phone_number', sa.String(),nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.create_foreign_key('votes_user_id_fkey', 'votes', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('post_users_fk', 'posts', 'user', ['owner_id'], ['id'], ondelete='CASCADE')
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###