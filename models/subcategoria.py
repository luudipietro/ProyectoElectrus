from database import db


class Subcategoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    id_categoria = db.Column(db.Integer, db.ForeignKey('Categoria.id'))