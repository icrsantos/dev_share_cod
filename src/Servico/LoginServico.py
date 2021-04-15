from src.Repositorio.UsuarioRepositorio import UsuarioRepositorio
from src.Entidades.Usuario import Usuario
import hashlib


def criar_usuario(usuario_json):
    usuario_repositorio = UsuarioRepositorio()
    usuario = Usuario()
    usuario_json["senha"] = encriptar_senha(usuario_json["senha"])
    usuario.definir_por_json(usuario_json)
    return usuario_repositorio.salvar(usuario)


def validar_usuario(usuario_json):
    usuario_repositorio = UsuarioRepositorio()
    nome = usuario_json['nome']
    senha = encriptar_senha(usuario_json['senha'])

    if not usuario_repositorio.validar(nome, senha):
        return False
    else:
        tupla = usuario_repositorio.buscar_por_nome_usuario(nome)
        usuario_logado = Usuario()
        usuario_logado.definir_por_tupla(tupla)
        return usuario_logado


def encriptar_senha(senha):
    senha_em_bytes = senha.encode('utf-8')
    hash_object = hashlib.sha1(senha_em_bytes)
    return hash_object.hexdigest()
