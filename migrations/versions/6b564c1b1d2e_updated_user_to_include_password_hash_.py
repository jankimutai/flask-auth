"""updated user to include password_hash and bcrypt encryption

Revision ID: 6b564c1b1d2e
Revises: 2ffd4cfb8f4d
Create Date: 2023-10-26 12:01:39.435318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b564c1b1d2e'
down_revision = '2ffd4cfb8f4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('_password_hash')

    # ### end Alembic commands ###