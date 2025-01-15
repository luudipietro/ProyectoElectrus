from idlelib.debugobj_r import remote_object_tree_item

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [
        {"id": 1, "nombre": "Producto 1", "price": "15.000", "imagen": "product1.jpg"},
        {"id": 2, "nombre": "Producto 2", "price": "3.000", "imagen": "product2.jpg"},
        {"id": 3, "nombre": "Producto 3", "price": "150.000", "imagen": "product3.jpg"},
        {"id": 4, "nombre": "Producto 5", "price": "245.000", "imagen": "product5.jpg"},
        {"id": 4, "nombre": "Producto 6", "price": "19.000", "imagen": "product6.jpg"},
        {"id": 4, "nombre": "Producto 7", "price": "19.000", "imagen": "product6.jpg"}
    ]
    return render_template('index.html', productos=productos)
@app.route('/productos')
def productos():
    categorias = [
        {"id":1, "nombre":"Línea Blanca"},
        {"id": 2, "nombre": "Pequeños Electrodomésticos"},
        {"id": 3, "nombre": "Cuidado Personal"},
        {"id": 4, "nombre": "Pequeños"},
        {"id": 5, "nombre": "gramdes"},
        {"id": 6, "nombre": "tuvi"},
        {"id": 7, "nombre": "yeña"},

    ]
    productos = [
        {"id": 1, "nombre": "Producto 1", "price": "15000", "imagen": "product1.jpg"},
        {"id": 2, "nombre": "Producto 2", "price": "3000", "imagen": "product2.jpg"},
        {"id": 3, "nombre": "Producto 3", "price": "150000", "imagen": "product3.jpg"},
        {"id": 4, "nombre": "Producto 5", "price": "245000", "imagen": "product5.jpg"},
        {"id": 4, "nombre": "Producto 6", "price": "19000", "imagen": "product6.jpg"},
        {"id": 4, "nombre": "Producto 7", "price": "19000", "imagen": "product6.jpg"},

    ]
    return render_template('productos.html', categorias=categorias, productos=productos)
@app.route('/colapsable')
def colapsable():
    return render_template('components/base.html')
if __name__ == '__main__':
    app.run(debug=True)
