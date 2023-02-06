"""create table Statuses

Revision ID: f12f30f03aa4
Revises: 9249a174fd6c
Create Date: 2023-02-05 15:51:55.230529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f12f30f03aa4'
down_revision = '9249a174fd6c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services_statuses_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Unicode(length=25), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.drop_table('services_status_list')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services_status_list',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='services_status_list_pkey'),
    sa.UniqueConstraint('id', name='services_status_list_id_key')
    )
    op.drop_table('services_statuses_list')
    # ### end Alembic commands ###
