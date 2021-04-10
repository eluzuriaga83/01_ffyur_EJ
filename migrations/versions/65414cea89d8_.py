"""empty message

Revision ID: 65414cea89d8
Revises: 79d621ea2608
Create Date: 2021-04-05 15:32:48.665901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65414cea89d8'
down_revision = '79d621ea2608'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres_artist', sa.ARRAY(sa.String()), nullable=False))
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.drop_column('Artist', 'genres_artist')
    # ### end Alembic commands ###