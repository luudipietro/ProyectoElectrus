from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [
        {"id": 1, "nombre": "Producto 1", "descripcion": "$15.000", "imagen": "product1.jpg"},
        {"id": 2, "nombre": "Producto 2", "descripcion": "$3.000", "imagen": "product2.jpg"},
        {"id": 3, "nombre": "Producto 3", "descripcion": "$150.000", "imagen": "product3.jpg"},
        {"id": 4, "nombre": "Producto 4", "descripcion": "$1.200", "imagen": "product4.jpg"},
        {"id": 4, "nombre": "Producto 5", "descripcion": "$245.000", "imagen": "product5.jpg"},
        {"id": 4, "nombre": "Producto 6", "descripcion": "$19.000", "imagen": "product6.jpg"},
        {"id": 4, "nombre": "Producto 7", "descripcion": "$19.000", "imagen": "product6.jpg"}
    ]
    return render_template('index.html', productos=productos)
@app.route('/carrusel')
def carrusel():
    return render_template('carrusel.html')
if __name__ == '__main__':
    app.run(debug=True)
