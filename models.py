from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from database import db

class Cliente(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    direccion = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    celular = Column(String(25))
    password_hash = Column(String(128), nullable=False)
    fecha_registro = Column(DateTime)

    # Relaciones
    ordenes = db.relationship('Orden', backref='cliente', lazy=True)
    carrito = db.relationship('Carrito', backref='cliente', lazy=True, uselist=False)  # Un solo carrito por cliente

class Carrito(db.Model):
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    detalles = db.relationship('DetalleCarrito', backref='carrito', lazy=True)

class DetalleCarrito(db.Model):
    id = Column(Integer, primary_key=True)
    id_carrito = Column(Integer, ForeignKey('carrito.id'), nullable=False)
    id_producto = Column(Integer, ForeignKey('producto.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)

class Orden(db.Model):
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    fecha = Column(DateTime, nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    estado = Column(String(200), nullable=False)

    # Relaciones
    detalles_orden = db.relationship('DetalleOrden', backref='orden', lazy=True)
    pagos = db.relationship('Pago', backref='orden', lazy=True)
    envios = db.relationship('Envio', backref='orden', lazy=True)

class DetalleOrden(db.Model):
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer, ForeignKey('orden.id'), nullable=False)
    id_producto = Column(Integer, ForeignKey('producto.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)

class Pago(db.Model):
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer, ForeignKey('orden.id'), nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    metodo = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)

class Envio(db.Model):
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer, ForeignKey('orden.id'), nullable=False)
    direccion = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)
    estado = Column(String(200), nullable=False)
    empresa = Column(String(200), nullable=False)

class Categoria(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)

    # Relación con Subcategorias
    subcategorias = db.relationship('Subcategoria', backref='categoria', lazy=True)

class Subcategoria(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    id_categoria = Column(Integer, ForeignKey('categoria.id'), nullable=False)

    # Relación con Productos
    productos = db.relationship('Producto', backref='subcategoria', lazy=True)

class Producto(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    peso = Column(Numeric(10, 2))
    dimensiones = Column(String(50))
    marca = Column(String(250))
    id_subcategoria = Column(Integer, ForeignKey('subcategoria.id'), nullable=False)

    # Relaciones con carrito y órdenes
    detalles_carrito = db.relationship('DetalleCarrito', backref='producto', lazy=True)
    detalles_orden = db.relationship('DetalleOrden', backref='producto', lazy=True)
