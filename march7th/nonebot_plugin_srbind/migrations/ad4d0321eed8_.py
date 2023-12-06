"""empty message

Revision ID: ad4d0321eed8
Revises: 32e7acac5b05
Create Date: 2023-10-18 14:28:37.017048

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ad4d0321eed8"
down_revision = "32e7acac5b05"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "nonebot_plugin_srbind_userbind", schema=None
    ) as batch_op:
        batch_op.add_column(sa.Column("device_id", sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column("device_fp", sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "nonebot_plugin_srbind_userbind", schema=None
    ) as batch_op:
        batch_op.drop_column("device_fp")
        batch_op.drop_column("device_id")

    # ### end Alembic commands ###
