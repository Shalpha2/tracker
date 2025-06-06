"""create table

Revision ID: eb5a40db6c9c
Revises: 86436b74cba1
Create Date: 2025-05-30 14:26:16.942847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb5a40db6c9c'
down_revision: Union[str, None] = '86436b74cba1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

   
def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=False),
    sa.Column('company', sa.String(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('applied_date', sa.Date(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_application')
    op.drop_table('users')
    op.drop_table('status')
    # ### end Alembic commands ###
