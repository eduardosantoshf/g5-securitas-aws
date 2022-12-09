"""change user id to string

Revision ID: 744c1deba10f
Revises: ceef96a6b0b2
Create Date: 2022-12-09 20:13:54.470137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744c1deba10f'
down_revision = 'ceef96a6b0b2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'id', type_=sa.String(150), existing_type=sa.INTEGER)



def downgrade() -> None:
    op.alter_column('users', 'id', type_=sa.INTEGER, existing_type=sa.VARCHAR)
