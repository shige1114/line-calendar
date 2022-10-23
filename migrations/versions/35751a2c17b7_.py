"""empty message

Revision ID: 35751a2c17b7
Revises: 05e42d559dbc
Create Date: 2022-10-21 22:26:20.440821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35751a2c17b7'
down_revision = '05e42d559dbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('voted_people', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'voted_people')
    # ### end Alembic commands ###
