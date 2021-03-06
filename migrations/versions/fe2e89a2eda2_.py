"""empty message

Revision ID: fe2e89a2eda2
Revises: a6e2a53f8246
Create Date: 2019-01-19 23:22:37.035838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe2e89a2eda2'
down_revision = 'a6e2a53f8246'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('validation_error',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('supplied_data_id', sa.String(), nullable=False),
    sa.Column('error_type', sa.String(length=50), nullable=False),
    sa.Column('summary', sa.String(length=200), nullable=False),
    sa.Column('details', sa.String(length=1000), nullable=False),
    sa.Column('line', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=200), nullable=True),
    sa.Column('occurrences', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplied_data_id'], ['supplied_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('supplied_data', sa.Column('validated', sa.Boolean(create_constraint=False), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplied_data', 'validated')
    op.drop_table('validation_error')
    # ### end Alembic commands ###
