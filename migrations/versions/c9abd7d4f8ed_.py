"""empty message

Revision ID: c9abd7d4f8ed
Revises: 06d58163acf9
Create Date: 2021-03-29 21:55:08.695381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9abd7d4f8ed'
down_revision = '06d58163acf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'id')
    # ### end Alembic commands ###
