"""sqllitechanges

Revision ID: c763f7ab6648
Revises: 
Create Date: 2024-10-16 17:02:45.972002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c763f7ab6648'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tertiaryapplication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Firstname', sa.String(), nullable=True),
    sa.Column('Middlename', sa.String(), nullable=True),
    sa.Column('Lastname', sa.String(), nullable=True),
    sa.Column('Gender', sa.String(), nullable=True),
    sa.Column('Phonenumber', sa.String(), nullable=True),
    sa.Column('Nationalid', sa.String(), nullable=True),
    sa.Column('GuardiansNo', sa.String(), nullable=True),
    sa.Column('Guardianid', sa.String(), nullable=True),
    sa.Column('Disability', sa.String(), nullable=True),
    sa.Column('Ward', sa.String(), nullable=True),
    sa.Column('Location', sa.String(), nullable=True),
    sa.Column('Sublocation', sa.String(), nullable=True),
    sa.Column('Village', sa.String(), nullable=True),
    sa.Column('Chiefname', sa.String(), nullable=True),
    sa.Column('Chiefphonenumber', sa.Integer(), nullable=True),
    sa.Column('AssistantChiefname', sa.String(), nullable=True),
    sa.Column('Assistantchiefno', sa.String(), nullable=True),
    sa.Column('Instituition', sa.String(), nullable=True),
    sa.Column('University', sa.String(), nullable=True),
    sa.Column('Amountexpecting', sa.String(), nullable=True),
    sa.Column('Amountreceived', sa.String(), nullable=True),
    sa.Column('Admno', sa.String(), nullable=True),
    sa.Column('levelofstudy', sa.String(), nullable=True),
    sa.Column('Modeofstudy', sa.String(), nullable=True),
    sa.Column('Yearofstudy', sa.String(), nullable=True),
    sa.Column('Semester', sa.String(), nullable=True),
    sa.Column('Coarseduration', sa.String(), nullable=True),
    sa.Column('Family', sa.String(), nullable=True),
    sa.Column('Fathersincome', sa.String(), nullable=True),
    sa.Column('Mothersincome', sa.String(), nullable=True),
    sa.Column('Approvalstatus', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Nationalid', sa.String(), nullable=True),
    sa.Column('Phonenumber', sa.String(), nullable=True),
    sa.Column('Role', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('tertiaryapplication')
    # ### end Alembic commands ###
