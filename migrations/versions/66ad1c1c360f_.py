"""empty message

Revision ID: 66ad1c1c360f
Revises: 2f9cd3035142
Create Date: 2018-10-13 10:52:10.858745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66ad1c1c360f'
down_revision = '2f9cd3035142'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('PublicId', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'PublicId')
    # ### end Alembic commands ###
