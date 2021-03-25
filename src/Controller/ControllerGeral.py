from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from src.Repositorio.PostagemRepositorio import PostagemRepositorio
from src.Servico import LoginServico, PostagemServico

app = Flask(__name__)
CORS(app)


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:63342'
    header['Access-Control-Allow-Credentials'] = 'true'
    header['Access-Control-Allow-Headers'] = '*'
    return response


@app.route('/api/login', methods=['POST'])
def validar_usuario():
    usuario_json = request.json
    LoginServico.validar_usuario(usuario_json)
    return str(LoginServico.validar_usuario(usuario_json))


@app.route('/api/usuario', methods=['POST'])
def criar_usuario():
    usuario_json = request.json
    id_usuario_criado = LoginServico.criar_usuario(usuario_json)
    return id_usuario_criado


@app.route('/api/postagem', methods=['POST'])
def criar_postagem():
    postagem_json = request.json
    id_postagem_criada = PostagemServico.criar_postagem(postagem_json)
    return id_postagem_criada


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
