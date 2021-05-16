from flask import Flask, jsonify, request
from flask_cors import CORS
from src.Servico import LoginServico, PostagemServico, NotificacaoServico

app = Flask(__name__)
CORS(app)


@app.after_request
def after_request(response):
    header = response.headers
    # header['Access-Control-Allow-Origin'] = 'http://localhost:63342'
    header['Access-Control-Allow-Origin'] = 'https://devsharecode.z13.web.core.windows.net'
    header['Access-Control-Allow-Credentials'] = 'true'
    header['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, X-CSRF-TOKEN'
    return response


@app.route('/api/login', methods=['POST'])
def validar_usuario():
    usuario_json = request.json
    return str(LoginServico.validar_usuario(usuario_json))


@app.route('/api/usuario', methods=['POST'])
def criar_usuario():
    usuario_json = request.json
    return LoginServico.criar_usuario(usuario_json)


@app.route('/api/postagem', methods=['POST'])
def criar_postagem():
    postagem_json = request.json
    return PostagemServico.criar_postagem(postagem_json)


@app.route('/api/postagem/<postagem_id>', methods=['GET'])
def buscar_postagem(postagem_id):
    return jsonify(PostagemServico.buscar_postagem_json(postagem_id))


@app.route('/api/postagem/respostas/<postagem_id>', methods=['GET'])
def buscar_perguntas_de_postagens(postagem_id):
    return jsonify(PostagemServico.buscar_respostas_de_postagem(postagem_id))


@app.route('/api/pesquisar/<pesquisa>', methods=['GET'])
def pesquisar_postagens(pesquisa):
    return jsonify(PostagemServico.pesquisar_postagens(pesquisa))


@app.route('/api/postagem/like/<usuario_id>/<postagem_id>', methods=['POST'])
def dar_like(usuario_id, postagem_id):
    return PostagemServico.curtir_postagem(usuario_id, postagem_id, True)


@app.route('/api/postagem/dislike/<usuario_id>/<postagem_id>', methods=['POST'])
def dar_dislike(usuario_id, postagem_id):
    return PostagemServico.curtir_postagem(usuario_id, postagem_id, False)


@app.route('/api/postagem/jaAvaliada/<usuario_id>/<postagem_id>', methods=['GET'])
def postagem_ja_curtida_por_usuario(usuario_id, postagem_id):
    return str(PostagemServico.postagem_ja_curtida_por_usuario(usuario_id, postagem_id))


@app.route('/api/postagem/usuario/<usuario_id>/perguntas', methods=['GET'])
def buscar_perguntas_usuario(usuario_id):
    return jsonify(PostagemServico.buscar_perguntas_de_usuario(usuario_id))


@app.route('/api/postagem/usuario/<usuario_id>/respostas', methods=['GET'])
def buscar_respostas_usuario(usuario_id):
    return jsonify(PostagemServico.buscar_respostas_de_usuario(usuario_id))


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


@app.route('/api/new-notifications/<usuario_id>', methods=['GET'])
def validar_novas_notificacoes(usuario_id):
    return NotificacaoServico.novas_notificacoes(usuario_id)


@app.route('/api/notifications/<usuario_id>', methods=['GET'])
def buscar_notificacoes(usuario_id):
    return jsonify(NotificacaoServico.buscar_notificacoes(usuario_id))


@app.route('/api/clean-notifications/<usuario_id>', methods=['GET'])
def limpar_notificacoes(usuario_id):
    return jsonify(NotificacaoServico.limpar_notificacoes(usuario_id))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
