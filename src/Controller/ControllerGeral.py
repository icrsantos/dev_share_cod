from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import src.Repositorio.UsuarioRepositorio

app = Flask(__name__)
CORS(app)

clientes = [
    {
        "nome": "João Paulo",
        "endereco": "Rua dos Amantes, nº 22",
        "celular": "(11) 98340-2877",
        "email": "joao.paulo@email.com",
        "cpf": "57652767091"
    },
    {
        "nome": "Ana Paula",
        "endereco": "Rua Vargas, nº 4",
        "celular": "(11) 98342-2877",
        "email": "ana.paula@email.com",
        "cpf": "32638871060"
    },
    {
        "nome": "Pedro André",
        "endereco": "Rua Caquinhos, nº 270",
        "celular": "(11) 98342-2877",
        "email": "pedro.andré@email.com",
        "cpf": "17315704060"
    }
]


@app.route('/api/usuario', methods=['GET'])
def validar_usuario():
    json_usuario = request.json
    return jsonify(clientes)


@app.route('/api/clientes', methods=['POST'])
def criar_clientes():
    json_request = request.json
    clientes.append(json_request)
    return jsonify({
        "id": str(len(clientes) - 1),
        "nome": str(json_request['nome'])
    })


@app.route('/api/clientes/<id_cliente>', methods=['DELETE'])
def deletar_clientes(id_cliente):
    clientes.pop(int(id_cliente))
    return jsonify({
        "status": "OK"
    })


@app.route('/api/clientes/<id_cliente>', methods=['PUT'])
def alterar_clientes(id_cliente):
    clientes[int(id_cliente)] = request.json
    return jsonify({
        "status": "OK"
    })


@app.route('/api/clientes/<id_cliente>', methods=['GET'])
def consultar_clientes(id_cliente):
    return clientes[int(id_cliente)]


if __name__ == '__main__':
    app.run(debug=True, port=5000)
