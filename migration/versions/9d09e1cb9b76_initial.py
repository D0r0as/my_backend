"""initial

Revision ID: 9d09e1cb9b76
Revises: 
Create Date: 2024-10-14 09:33:50.162970

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '9d09e1cb9b76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('meals',
    sa.Column('id_meal', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('count_ingredients', sa.Integer(), nullable=False),
    sa.Column('gruppa', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('season', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('weigth', sa.Integer(), nullable=False),
    sa.Column('count_pors', sa.Integer(), nullable=False),
    sa.Column('prepering_time', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_meal'),
    schema=settings.POSTGRES_SCHEMA
    )


def downgrade():
    op.drop_table('meals', schema=settings.POSTGRES_SCHEMA)
