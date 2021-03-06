"""empty message

Revision ID: 56266fea47a8
Revises: b7883bb1c94e
Create Date: 2020-02-21 00:07:36.086272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56266fea47a8'
down_revision = 'b7883bb1c94e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'seeking_venue')
    # ### end Alembic commands ###
