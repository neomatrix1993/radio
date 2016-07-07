"""Create message_requests table

Revision ID: 5d7388b01dd8
Revises: efb80846f59f
Create Date: 2016-07-07 12:34:22.583726

"""

# revision identifiers, used by Alembic.
revision = '5d7388b01dd8'
down_revision = 'efb80846f59f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('message_requests',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('request_id', sa.Integer, sa.ForeignKey('requests.id'), nullable=False),
                    sa.Column('user_id', sa.Integer, nullable=False),
                    sa.Column('target', sa.String(256), nullable=False),
                    sa.Column('template_id', sa.Integer, sa.ForeignKey('templates.id'), nullable=False),
                    sa.Column('payload', sa.Text, nullable=False),
                    sa.Column('from_ts', sa.TIMESTAMP, nullable=True),
                    sa.Column('end_ts', sa.TIMESTAMP, nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('message_requests')
