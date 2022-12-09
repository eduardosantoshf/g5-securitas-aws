"""change intrusions and properties user_id from int to string

Revision ID: 9ac572c008c5
Revises: 744c1deba10f
Create Date: 2022-12-09 20:40:44.614205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ac572c008c5'
down_revision = '744c1deba10f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('properties', 'owner_id', type_=sa.String(150), existing_type=sa.INTEGER)
    op.alter_column('intrusions', 'user_id', type_=sa.String(150), existing_type=sa.INTEGER)
    op.create_foreign_key(None, 'properties', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'intrusions', 'users', ['user_id'], ['id'], ondelete='CASCADE')

def downgrade() -> None:
    op.drop_constraint(None, 'properties', type_='foreignkey')
    op.drop_constraint(None, 'intrusions', type_='foreignkey')
    op.alter_column('properties', 'id', type_=sa.String(150), existing_type=sa.INTEGER)
    op.alter_column('intrusions', 'id', type_=sa.String(150), existing_type=sa.INTEGER)
