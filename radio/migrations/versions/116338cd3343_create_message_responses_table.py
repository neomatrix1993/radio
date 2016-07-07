"""Create message_responses table

Revision ID: 116338cd3343
Revises: 5d7388b01dd8
Create Date: 2016-07-07 14:38:21.658296

"""

# revision identifiers, used by Alembic.
revision = '116338cd3343'
down_revision = '5d7388b01dd8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('message_responses',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('message_request_id', sa.Integer, sa.ForeignKey('message_requests.id'), nullable=False),
                    sa.Column('provider', sa.String(64), nullable=False),
                    sa.Column('response_data', sa.Text, nullable=False),
                    sa.Column('delivered_at', sa.TIMESTAMP, nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('message_responses')
