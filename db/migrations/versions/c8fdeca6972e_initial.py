"""initial

Revision ID: c8fdeca6972e
Revises: 
Create Date: 2023-11-08 23:17:54.245973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8fdeca6972e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('danger',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('shots', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('suspenders', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('danger_level', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_danger')),
    sa.UniqueConstraint('id', name=op.f('uq_danger_id'))
    )
    op.create_table('human',
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('middle_name', sa.Text(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('danger_level', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_human')),
    sa.UniqueConstraint('id', name=op.f('uq_human_id'))
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('human')
    op.drop_table('danger')
    # ### end Alembic commands ###