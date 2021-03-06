"""empty message

Revision ID: 3a0288c18cbc
Revises: 13227fcc257a
Create Date: 2016-10-15 05:42:06.192041

"""

# revision identifiers, used by Alembic.
revision = '3a0288c18cbc'
down_revision = '13227fcc257a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('icon', sa.String(length=80), nullable=False),
    sa.Column('color', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('icon'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('color')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'categories', type_='unique')
    op.drop_column('categories', 'color')
    ### end Alembic commands ###
