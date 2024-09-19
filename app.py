from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    productos = [
        {'id': 1, 'nombre': 'Producto 1', 'precio': 20, 'imagen': 'producto1.jpg'},
        {'id': 2, 'nombre': 'Producto 2', 'precio': 25, 'imagen': 'producto1.jpg'},
        {'id': 3, 'nombre': 'Producto 3', 'precio': 30, 'imagen': 'producto1.jpg'}
    ]
    return render_template('index.html', productos=productos)

# Ruta para ver detalles de un producto
@app.route('/producto/<int:id>')
def producto(id):
    # Datos de ejemplo del producto
    producto = {'id': id, 'nombre': f'Producto {id}', 'precio': 20 * id, 'descripcion': 'Descripción del producto', 'imagen': 'producto1.jpg'}
    return render_template('product.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
