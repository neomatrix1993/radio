"""Create templates table

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
    op.create_table('templates',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('name', sa.String(128), nullable=False),
                    sa.Column('description', sa.String(256), nullable=False),
                    sa.Column('body', sa.Text, nullable=False),
                    sa.Column('version', sa.Integer, nullable=False),
                    sa.Column('handler', sa.String(16), nullable=False),
                    sa.Column('is_enabled', sa.Boolean, nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('templates')
