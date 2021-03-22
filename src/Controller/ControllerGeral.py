from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from src.Repositorio.UsuarioRepositorio import UsuarioRepositorio
from src.Repositorio.PostagemRepositorio import PostagemRepositorio
from src.Entidades.Usuario import Usuario
from src.Entidades.Postagem import Postagem

app = Flask(__name__)
CORS(app)


@app.route('/api/usuario', methods=['GET'])
def validar_usuario():
    json_usuario = request.json
    return 'OK'


@app.route('/api/usuario', methods=['POST'])
def criar_usuario():
    json_request = request.json
    usuario_repositorio = UsuarioRepositorio()
    usuario = Usuario(
        json_request['nome'],
        json_request["email"],
        json_request['senha']
    )
    return usuario_repositorio.salvar(usuario)


@app.route('/api/pesquisar/<pesquisa>', methods=['GET'])
def pesquisar_postagens(pesquisa):
    postagem_repositorio = PostagemRepositorio()
    return postagem_repositorio.buscar_postagens(pesquisa)


@app.route('/api/clientes/<id_cliente>', methods=['DELETE'])
def deletar_clientes(id_cliente):
    return jsonify({
        "status": "OK"
    })


@app.route('/api/clientes/<id_cliente>', methods=['PUT'])
def alterar_clientes(id_cliente):
    return jsonify({
        "status": "OK"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
