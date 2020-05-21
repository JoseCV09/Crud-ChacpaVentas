from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from UsuarioDAO import Usuario
from ProductoDao import Producto
from ClienteDao import Cliente
user = Usuario()
prod = Producto()
cli = Cliente()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje': 'Bienvenidos a Flask'})


@app.route('/usuario/listar', methods=['GET'])
def users():
    try:
        rows = user.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


@app.route('/usuario/buscar/<int:id>')
def buscarusuario(id):
	try:
		user.idusuario = id
		row = user.buscarusuario()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)


@app.route('/usuario/create', methods=['POST'])
def agregarusuario():
    try:
        _json = request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        if request.method=='POST':
            resp=user.agregarusuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/usuario/eliminar/<int:id>', methods=['GET'])
def eliminarusuario(id):
    try:
        user.idusuario=id
        resp=user.delete()
        resp=jsonify('Usuario Elimindado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)    
@app.route('/usuario/modificar', methods=['PUT'])
def modificarusuario():
    try:
        _json=request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        user.idusuario=_json['iduser']
        if request.method == 'PUT':
            resp = user.modificarusuario()
            resp = jsonify('Usuario Modificada')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)


'''PRODUCTO'''

@app.route('/producto/listar', methods=['GET'])
def prods():
    try:
        rows = prod.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/producto/buscar/<int:id>')
def buscarproducto(id):
	try:
		prod.id_producto = id
		row = prod.buscarproducto()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@app.route('/producto/create', methods=['POST'])
def agregarproducto():
    try:
        _json = request.json
        prod.nombre_producto=_json['nom']
        prod.precio=_json['pre']
        prod.cantidad=_json['cant']
        if request.method=='POST':
            resp=prod.agregarproducto()
            resp=jsonify('producto')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)


@app.route('/producto/eliminar/<int:id>', methods=['GET'])
def eliminarproducto(id):
    try:
        prod.id_producto=id
        resp=prod.deleteproducto()
        resp=jsonify('Producto Eliminado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e) 


@app.route('/producto/modificar', methods=['PUT'])
def modificarproducto():
    try:
        _json=request.json
        prod.nombre_producto=_json['nom_prod']
        prod.precio=_json['pre']
        prod.cantidad=_json['cant']
        prod.estado=_json['est']
        prod.id_producto=_json['idp']
        if request.method == 'PUT':
            resp = prod.modificarproducto()
            resp = jsonify('Producto Modificado')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)


'''CLIENTE'''

@app.route('/cliente/listar', methods=['GET'])
def clients():
    try:
        rows = cli.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


@app.route('/cliente/buscar/<int:id>')
def buscarcliente(id):
	try:
		cli.id_cliente = id
		row = cli.buscarcliente()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)


@app.route('/cliente/create', methods=['POST'])
def agregarcliente():
    try:
        _json = request.json
        cli.nombre_cliente=_json['nombre_cliente']
        cli.apellido_cliente=_json['apellido_cliente']
        cli.dni=_json['dni']
        cli.correo = _json['correo']
        cli.direccion = _json['direccion']
        cli.telefono = _json['telefono']
        if request.method=='POST':
            resp=cli.agregarcliente()
            resp=jsonify('Cliente Agregado')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)


@app.route('/cliente/eliminar/<int:id>', methods=['GET'])
def eliminarcliente(id):
    try:
        cli.id_cliente=id
        resp=cli.deletecliente()
        resp=jsonify('Cliente Eliminado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e) 


@app.route('/cliente/modificar', methods=['PUT'])
def modificarcliente():
    try:
        _json=request.json
        cli.nombre_cliente=_json['nombre_cliente']
        cli.apellido_cliente=_json['apellido_cliente']
        cli.dni=_json['dni']
        cli.correo=_json['correo']
        cli.direccion=_json['direccion']
        cli.telefono=_json['telefono']
        cli.id_cliente=_json['id_cliente']
        if request.method == 'PUT':
            resp = cli.modificarcliente()
            resp = jsonify('Cliente Modificado')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True) 

