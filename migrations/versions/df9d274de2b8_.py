"""empty message

Revision ID: df9d274de2b8
Revises: 846a84fd4443
Create Date: 2018-10-28 16:40:06.336678

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'df9d274de2b8'
down_revision = '846a84fd4443'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tickets', 'ArrivalDate')
    op.drop_column('tickets', 'ArrivalTime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('ArrivalTime', postgresql.TIME(), autoincrement=False, nullable=True))
    op.add_column('tickets', sa.Column('ArrivalDate', sa.DATE(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
