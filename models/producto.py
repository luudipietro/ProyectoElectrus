from database import db
from sqlalchemy import DECIMAL

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    precio = db.Column(DECIMAL(10, 2))
    stock = db.Column(db.String(250))
    id_categoria
    imagenes = db.Column(db.Integer)

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'nombre: {self.nombre}, '
            f'descripcion: {self.descripcion}, '
            f'stock: {self.stock}, '
            f'precio: {self.precio} '
        )



class Subcategoria(db.Model):
    id
