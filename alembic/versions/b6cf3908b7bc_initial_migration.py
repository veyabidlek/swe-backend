"""Initial migration

Revision ID: b6cf3908b7bc
Revises: beb01bf1fd17
Create Date: 2024-12-01 15:54:42.101648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6cf3908b7bc'
down_revision: Union[str, None] = 'beb01bf1fd17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery_methods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_delivery_methods_id'), 'delivery_methods', ['id'], unique=False)
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_id'), 'messages', ['id'], unique=False)
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['buyers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('buyer_id')
    )
    op.create_index(op.f('ix_carts_id'), 'carts', ['id'], unique=False)
    op.create_table('cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_items_id'), 'cart_items', ['id'], unique=False)
    op.create_table('offers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.Column('proposed_price', sa.Float(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['buyers.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_offers_id'), 'offers', ['id'], unique=False)
    op.add_column('buyers', sa.Column('balance', sa.Float(), nullable=True))
    op.drop_constraint(None, 'buyers', type_='foreignkey')
    op.create_foreign_key(None, 'buyers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('deliveries', sa.Column('delivery_method_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'deliveries', 'delivery_methods', ['delivery_method_id'], ['id'])
    op.add_column('farmers', sa.Column('balance', sa.Float(), nullable=True))
    op.drop_constraint(None, 'farmers', type_='foreignkey')
    op.create_foreign_key(None, 'farmers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'farmers', type_='foreignkey')
    op.create_foreign_key(None, 'farmers', 'users', ['user_id'], ['id'])
    op.drop_column('farmers', 'balance')
    op.drop_constraint(None, 'deliveries', type_='foreignkey')
    op.drop_column('deliveries', 'delivery_method_id')
    op.drop_constraint(None, 'buyers', type_='foreignkey')
    op.create_foreign_key(None, 'buyers', 'users', ['user_id'], ['id'])
    op.drop_column('buyers', 'balance')
    op.drop_index(op.f('ix_offers_id'), table_name='offers')
    op.drop_table('offers')
    op.drop_index(op.f('ix_cart_items_id'), table_name='cart_items')
    op.drop_table('cart_items')
    op.drop_index(op.f('ix_carts_id'), table_name='carts')
    op.drop_table('carts')
    op.drop_index(op.f('ix_messages_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_delivery_methods_id'), table_name='delivery_methods')
    op.drop_table('delivery_methods')
    # ### end Alembic commands ###
