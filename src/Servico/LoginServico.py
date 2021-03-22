from src.Repositorio.UsuarioRepositorio import UsuarioRepositorio
from src.Entidades.Usuario import Usuario
import hashlib


def criar_usuario(usuario_json):
    usuario_repositorio = UsuarioRepositorio()
    usuario = Usuario(
        usuario_json['nome'],
        usuario_json["email"],
        encriptar_senha(usuario_json['senha'])
    )
    return usuario_repositorio.salvar(usuario)


def validar_usuario(usuario_json):
    usuario_repositorio = UsuarioRepositorio()
    nome = usuario_json['nome']
    senha = encriptar_senha(usuario_json['senha'])
    return usuario_repositorio.validar(nome, senha)


def encriptar_senha(senha):
    senha_em_bytes = senha.encode('utf-8')
    hash_object = hashlib.sha1(senha_em_bytes)
    return hash_object.hexdigest()
