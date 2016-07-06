"""initial tables

Revision ID: 051f721d8209
Revises:
Create Date: 2016-07-06 14:45:08.752384

"""

# revision identifiers, used by Alembic.
revision = '051f721d8209'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('test',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('data', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('test')
