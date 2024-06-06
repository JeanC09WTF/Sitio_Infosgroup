#importaciones
from flask import Flask, render_template
import json

#aplicacion inicial 
app = Flask(__name__, static_url_path='/static')

def cargar_productos():
    with open('productos.json', 'r', encoding='utf-8') as archivo:
        productos = json.load(archivo)
    return productos

#Rutas
@app.route('/') #Decorador 
def index():
   productos = cargar_productos()
   return render_template('base.html', products=productos)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html')

# Función para obtener un producto por su ID
def obtener_producto_por_id(productos, producto_id):
    for producto in productos:
        if producto.get('id') == producto_id:
            return producto
    return 404

# Ruta para la página de detalles del producto
@app.route('/ver_mas/<int:producto_id>')
def ver_mas(producto_id):
    productos = cargar_productos()
    producto = obtener_producto_por_id(productos, producto_id)
    if producto:
        return render_template('detalle_producto.html', producto=producto)
    else:
        return 'Producto no encontrado', 404


#correr aplicacion
if __name__ == '__main__':
   app.run(debug=True, port=3000)