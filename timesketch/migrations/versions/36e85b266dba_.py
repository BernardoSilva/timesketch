"""empty message

Revision ID: 36e85b266dba
Revises: be32626451fb
Create Date: 2016-09-06 10:45:09.136810

"""
# This code is auto generated. Ignore linter errors.
# pylint: skip-file

# revision identifiers, used by Alembic.
revision = '36e85b266dba'
down_revision = 'be32626451fb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('view', sa.Column('query_dsl', sa.UnicodeText(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('view', 'query_dsl')
    ### end Alembic commands ###
