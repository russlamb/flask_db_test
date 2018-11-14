"""my text table

Revision ID: c503d95c7a43
Revises: 
Create Date: 2018-11-13 16:37:19.753477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c503d95c7a43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.String(length=32), nullable=True),
    sa.Column('session_text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_my_text_session_id'), 'my_text', ['session_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_my_text_session_id'), table_name='my_text')
    op.drop_table('my_text')
    # ### end Alembic commands ###