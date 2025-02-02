"""agregado cantidad de imagenes

Revision ID: d88223dcd109
Revises: 
Create Date: 2025-01-29 12:56:14.105109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd88223dcd109'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('celular', sa.String(length=25), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('fecha_registro', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carrito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_cliente'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('total', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['id_cliente'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subcategoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('id_categoria', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_categoria'], ['categoria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('envio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_orden', sa.Integer(), nullable=False),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('empresa', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['id_orden'], ['orden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pago',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_orden', sa.Integer(), nullable=False),
    sa.Column('monto', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('metodo', sa.String(length=250), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_orden'], ['orden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=False),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('imagenes', sa.Integer(), nullable=True),
    sa.Column('dimensiones', sa.String(length=50), nullable=True),
    sa.Column('marca', sa.String(length=250), nullable=True),
    sa.Column('id_subcategoria', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_subcategoria'], ['subcategoria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detalle_carrito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_carrito', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_carrito'], ['carrito.id'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detalle_orden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_orden', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('precio_unitario', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id_orden'], ['orden.id'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detalle_orden')
    op.drop_table('detalle_carrito')
    op.drop_table('producto')
    op.drop_table('pago')
    op.drop_table('envio')
    op.drop_table('subcategoria')
    op.drop_table('orden')
    op.drop_table('carrito')
    op.drop_table('cliente')
    op.drop_table('categoria')
    # ### end Alembic commands ###
