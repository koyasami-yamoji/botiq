"""create_table

Revision ID: 72758c2d50b4
Revises: 
Create Date: 2023-07-31 15:14:20.784544

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72758c2d50b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('history',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=False),
                    sa.Column('date_time', sa.DateTime(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('command', sa.String(), nullable=False),
                    sa.Column('check_in', sa.Date(), nullable=False),
                    sa.Column('check_out', sa.Date(), nullable=False),
                    sa.Column('min_price', sa.Integer(), nullable=True),
                    sa.Column('max_price', sa.Integer(), nullable=True),
                    sa.Column('min_distance', sa.Integer(), nullable=True),
                    sa.Column('max_distance', sa.Integer(), nullable=True),
                    sa.Column('count_hotels', sa.Integer(), nullable=False),
                    sa.Column('count_photo', sa.Integer(), nullable=False),
                    sa.Column('destination_id', sa.BigInteger(), nullable=False),
                    sa.Column('sort', sa.String(), nullable=False),
                    )
    op.create_index(op.f('ix_history_user_id'), 'history', ['user_id'], unique=False)
    op.create_table('photo',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
                    sa.Column('hotel_id', sa.BigInteger(), nullable=False),
                    sa.Column('photo', sa.String(), nullable=False),
                    )
    op.create_index(op.f('ix_photo_hotel_id'), 'photo', ['hotel_id'], unique=False)
    op.create_table('hotels',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('history_id', sa.Integer(), nullable=False),
                    sa.Column('hotel_id', sa.BigInteger(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.Column('price', sa.Numeric(), nullable=False),
                    sa.Column('distance', sa.Numeric(), nullable=False),
                    sa.Column('user_rates', sa.Numeric(), nullable=True),
                    sa.ForeignKeyConstraint(['history_id'], ['history.id'], ondelete='CASCADE'),
                    )
    op.create_index(op.f('ix_hotels_history_id'), 'hotels', ['history_id'], unique=False)
    op.create_index(op.f('ix_hotels_hotel_id'), 'hotels', ['hotel_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_hotels_hotel_id'), table_name='hotels')
    op.drop_index(op.f('ix_hotels_history_id'), table_name='hotels')
    op.drop_table('hotels')
    op.drop_index(op.f('ix_photo_hotel_id'), table_name='photo')
    op.drop_table('photo')
    op.drop_index(op.f('ix_history_telegram_id'), table_name='history')
    op.drop_table('history')
