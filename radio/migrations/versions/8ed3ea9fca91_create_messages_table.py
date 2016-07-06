"""Create messages table

Revision ID: 8ed3ea9fca91
Revises: 051f721d8209
Create Date: 2016-07-06 16:52:05.769253

"""

# revision identifiers, used by Alembic.
revision = '8ed3ea9fca91'
down_revision = '051f721d8209'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('messages',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('template_id', sa.Integer, nullable=False),
                    sa.Column('target', sa.Text, nullable=False),
                    sa.Column('payload', sa.Text, nullable=False),
                    sa.Column('expiration', sa.Timestamp, nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('messages')
