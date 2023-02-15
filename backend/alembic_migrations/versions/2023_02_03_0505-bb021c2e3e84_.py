"""

Revision ID: bb021c2e3e84
Revises: adc9523a77fd
Create Date: 2023-02-03 05:05:48.199074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb021c2e3e84'
down_revision = 'adc9523a77fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('media', sa.Column('inoculation_type', sa.String(), nullable=True))
    op.drop_constraint('spawn_media_id_fkey', 'spawn', type_='foreignkey')
    op.drop_column('spawn', 'media_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spawn', sa.Column('media_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('spawn_media_id_fkey', 'spawn', 'media', ['media_id'], ['id'])
    op.drop_column('media', 'inoculation_type')
    # ### end Alembic commands ###
