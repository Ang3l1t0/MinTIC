from flask import Flask
from flask import jsonify
from flask import request
from productos import productos

app = Flask(__name__)


@app.route('/')
def index():
    return 'Ento a la raiz'


@app.route('/productos')
def get_productos():
    return jsonify({"productos": productos})


@app.route('/productos/<string:nom_producto>')
def get_producto(nom_producto):
    list_productos = [
        producto for producto in productos if producto['nombre'] == nom_producto]
    if len(list_productos) > 0:
        return jsonify({"producto":  list_productos})
    return jsonify({"mensaje": "Producto {} no encontrado".format(nom_producto)})


@app.route('/productos', methods=['POST'])
def add_producto():
    producto = request.json
    productos.append(producto)
    return jsonify({"mensaje": "producto {} agregado".format(producto["nombre"]), "productos": productos})


@app.route('/productos/<string:nom_producto>', methods=['PUT'])
def update_producto(nom_producto):
    # Buscar el producto
    lista_productos = [
        producto for producto in productos if producto["nombre"] == nom_producto]
    if len(lista_productos) > 0:
        producto = lista_productos[0]
        # actualizar
        producto['nombre'] = request.json['nombre']
        producto['precio'] = request.json['precio']
        producto['cantidad'] = request.json['cantidad']

        # mensaje
        return jsonify({"mensaje": "Producto {} actualizado".format(nom_producto), "productos": productos})
    else:
        return jsonify({"mensaje": "Producto {} no encontrado".format(nom_producto), "productos": productos})


@app.route('/productos/<string:nom_producto>', methods=['DELETE'])
def delete_producto(nom_producto):
    lista_productos = [
        producto for producto in productos if producto["nombre"] == nom_producto]
    if len(lista_productos) > 0:
        productos.remove(lista_productos[0])
        return jsonify({"mensaje": "Producto {} eliminado".format(nom_producto), "productos": productos})
    return jsonify({"mensaje": "Producto {} no fue encontrado".format(nom_producto), "productos": productos})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
