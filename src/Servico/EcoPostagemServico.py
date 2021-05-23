import json

from src.Entidades.EcoPostagem import EcoPostagem
from src.Repositorio.EcoPostagemRepositorio import EcoPostagemRepositorio
from src.Servico import NotificacaoServico, UsuarioServico, PostagemServico


def criar_eco(usuario_id, postagem_id):
    id_eco = salvar(usuario_id, postagem_id)
    usuario = UsuarioServico.buscar_por_id(usuario_id)
    postagem_ecoada = PostagemServico.buscar_postagem_por_id(postagem_id)
    postagem_ecoada.relevancia = postagem_ecoada.relevancia + 10
    PostagemServico.criar_ou_atualizar(postagem_ecoada)
    NotificacaoServico.notificar_eco_de_postagem(usuario, postagem_ecoada)
    return id_eco


def buscar(usuario_id, postagem_id):
    eco_repositorio = EcoPostagemRepositorio()
    eco = EcoPostagem()
    tupla = eco_repositorio.buscar(usuario_id, postagem_id)
    eco.definir_por_tupla(tupla)
    return eco


def buscar_json(usuario_id, postagem_id):
    eco = buscar(usuario_id, postagem_id)
    return eco.json()


def buscar_ecos_por_postagem_id(postagem_id):
    eco_repositorio = EcoPostagemRepositorio()
    tuplas = eco_repositorio.buscar_por_postagem_id(postagem_id)
    return __lista_tuplas_para_lista_entidade(tuplas)


def salvar(usuario_id, postagem_id):
    eco_repositorio = EcoPostagemRepositorio()
    eco = EcoPostagem()
    eco.usuario_id = usuario_id
    eco.postagem_id = postagem_id
    return eco_repositorio.salvar(eco)


def eco_existe(usuario_id, postagem_id):
    eco_repositorio = EcoPostagemRepositorio()
    tupla = eco_repositorio.buscar(usuario_id, postagem_id)
    return tupla is not None


def remover_eco_postagem(usuario_id, postagem_id):
    postagem = PostagemServico.buscar_postagem_por_id(postagem_id)
    postagem.relevancia = postagem.relevancia - 10
    PostagemServico.criar_ou_atualizar(postagem)
    return __remover_eco(usuario_id, postagem_id)


def __remover_eco(usuario_id, postagem_id):
    eco_repositorio = EcoPostagemRepositorio()
    if eco_existe(usuario_id, postagem_id):
        eco = buscar(usuario_id, postagem_id)
        eco_repositorio.remover(eco)
    return True


def __buscar_ecos_postagem_json(postagem_id):
    eco_repositorio = EcoPostagemRepositorio()
    tuplas = eco_repositorio.buscar_por_postagem_id(postagem_id)
    return __lista_tuplas_para_lista_json(tuplas)


def __lista_tuplas_para_lista_json(tuplas):
    lista_ecos = ''
    if len(tuplas) == 0:
        return []
    if len(tuplas) >= 1:
        lista_ecos += '[\n'
    for tupla in tuplas:
        eco = EcoPostagem()
        eco.definir_por_tupla(tupla)
        lista_ecos += eco.json_string()
        if tuplas.index(tupla) != (len(tuplas) - 1):
            lista_ecos += '\t,\n'
    if len(tuplas) >= 1:
        lista_ecos += ']'
    return json.loads(lista_ecos)


def __lista_tuplas_para_lista_entidade(tuplas):
    lista_ecos = []
    for tupla in tuplas:
        eco = EcoPostagem()
        eco.definir_por_tupla(tupla)
        lista_ecos.append(eco)
    return lista_ecos
