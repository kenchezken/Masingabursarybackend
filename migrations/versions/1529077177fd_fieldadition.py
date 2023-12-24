"""fieldadition

Revision ID: 1529077177fd
Revises: 28bdca72c126
Create Date: 2023-12-23 16:46:09.768453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1529077177fd'
down_revision = '28bdca72c126'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tertiaryapplication', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Firstname', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Middlename', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Lastname', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Guardianid', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Chiefname', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Chiefphonenumber', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('AssistantChiefname', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Amountexpecting', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('Amountreceived', sa.String(), nullable=True))
        batch_op.drop_column('Motherid')
        batch_op.drop_column('Fullname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tertiaryapplication', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Fullname', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Motherid', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('Amountreceived')
        batch_op.drop_column('Amountexpecting')
        batch_op.drop_column('AssistantChiefname')
        batch_op.drop_column('Chiefphonenumber')
        batch_op.drop_column('Chiefname')
        batch_op.drop_column('Guardianid')
        batch_op.drop_column('Lastname')
        batch_op.drop_column('Middlename')
        batch_op.drop_column('Firstname')

    # ### end Alembic commands ###
