"""Initial Migration

Revision ID: 91570909d124
Revises: 
Create Date: 2021-09-22 17:44:20.626825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91570909d124'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('pitch', sa.Text(), nullable=True),
    sa.Column('publishedtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###
