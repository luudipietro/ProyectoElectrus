from sqlalchemy.orm import relationship

from database import db


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))

    subcategorias = relationship('Subcategoria', backref='Categoria', lazy=True)
