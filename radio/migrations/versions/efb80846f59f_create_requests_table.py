"""Create requests table

Revision ID: efb80846f59f
Revises: 8ed3ea9fca91
Create Date: 2016-07-07 12:32:00.541878

"""

# revision identifiers, used by Alembic.
revision = 'efb80846f59f'
down_revision = '8ed3ea9fca91'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('requests',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('request_body', sa.Text, nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('requests')
