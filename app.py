
from config import Config
from flask_migrate import Migrate
from flask import Flask, render_template

from database import db
from models import Producto

app = Flask(__name__)
app.config.from_object(Config)  # Cargar la configuración

@app.route('/')
def inicio():
    productos = Producto.query.all()
    total_productos = Producto.query.count()
    for producto in productos:
        app.logger.debug(f'producto: {producto}')
    return render_template('index.html', productos=productos, total_productos=total_productos)
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
        {"id": 1, "nombre": "Placa de Video Zotac GeForce RTX 4060 Ti 16GB GDDR6 AMP", "price": "662130", "imagen": "placa3.jpg"},
        {"id": 2, "nombre": "Producto 2", "price": "3000", "imagen": "product2.jpg"},
        {"id": 3, "nombre": "Producto 3", "price": "150000", "imagen": "product3.jpg"},
        {"id": 4, "nombre": "Producto 5", "price": "245000", "imagen": "product5.jpg"},
        {"id": 4, "nombre": "Producto 6", "price": "19000", "imagen": "product6.jpg"},
        {"id": 4, "nombre": "Producto 7", "price": "19000", "imagen": "product6.jpg"},

    ]
    return render_template('productos.html', categorias=categorias, productos=productos)
@app.route('/carrito')
def carrito():
    productos = [


    ]
    return render_template('carrito.html', carrito=productos)


@app.route('/producto/<int:id>')
def producto(id):
    product = {
        "name": "Placa de Video Zotac GeForce RTX 4060 Ti 16GB GDDR6 AMP",
        "price_special": 662130,
        "price_list": 926963,
        "installment_price": 77247,
        "warranty": "12 meses",
        "stock_status": "Disponible",
        "shipping": "Envíos a todo el país",
        "features": {
            "Tipo": "pcie",
            "Chipset GPU": "RTX 4060 Ti",
            "Entrada Video": "No",
            "Puente Para Sli/crossfirex": "-",
            "Doble Puente": "No",
        },
        "connectivity": {
            "VGA": 0,
            "DVI Digital": 0,
            "HDMI": 1,
            "DisplayPorts": 3,
        },
        "images": ["placa1.jpg", "placa2.jpg","placa3.jpg", "placa4.jpg", "placa5.jpg"],
        "description":"La NVIDIA GeForce RTX 4060 Ti es una tarjeta gráfica de gama media-alta de la generación Ada Lovelace, diseñada para ofrecer un excelente rendimiento en gaming y creación de contenido con tecnologías avanzadas de NVIDIA, como el trazado de rayos (Ray Tracing) y la IA impulsada por DLSS 3."
    }
    return render_template('producto.html', product=product)

@app.template_filter('format_precio')
def format_precio(value):
    """ Formatea el número con puntos como separador de miles y coma para los decimales. """
    try:
        return "{:,.2f}".format(float(value)).replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value  # Retorna el valor sin formato si hay un error

# Registro del filtro
app.jinja_env.filters['format_precio'] = format_precio

#inicializacion del objeto db de sqlachemy
db.init_app(app)

#configurar flask migrate
migrate = Migrate()
migrate.init_app(app, db)


if __name__ == '__main__':
    app.run(debug=True)
