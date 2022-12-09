"""delete all constraints

Revision ID: ceef96a6b0b2
Revises: 948d7dcd460b
Create Date: 2022-12-09 19:41:04.687601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceef96a6b0b2'
down_revision = '948d7dcd460b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE intrusions DROP FOREIGN KEY intrusions_ibfk_1;")
    op.execute("ALTER TABLE properties DROP FOREIGN KEY properties_ibfk_1;")
    

def downgrade() -> None:
    pass
