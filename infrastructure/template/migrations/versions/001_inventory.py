"""Initial relational inventory schema."""
from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("categories", sa.Column("id", sa.Integer(), primary_key=True),
                    sa.Column("name", sa.String(80), nullable=False, unique=True))
    op.create_table("items", sa.Column("id", sa.Integer(), primary_key=True),
                    sa.Column("name", sa.String(80), nullable=False, unique=True),
                    sa.Column("category_id", sa.Integer(), sa.ForeignKey("categories.id"), nullable=False))
    op.create_index("ix_items_category_id", "items", ["category_id"])


def downgrade():
    op.drop_table("items")
    op.drop_table("categories")
