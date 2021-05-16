import json

from src.Repositorio.UsuarioRepositorio import UsuarioRepositorio
from src.Entidades.Usuario import Usuario


def buscar_por_id(usuario_id):
    usuario_repositorio = UsuarioRepositorio()
    tupla = usuario_repositorio.buscar_por_id(usuario_id)
    usuario = Usuario()
    usuario.definir_por_tupla(tupla)
    return usuario


def buscar_nome_usuario_por_id(usuario_id):
    usuario = buscar_por_id(usuario_id)
    return usuario.nome
