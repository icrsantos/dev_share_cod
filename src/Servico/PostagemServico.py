import json

from src.Repositorio.PostagemRepositorio import PostagemRepositorio
from src.Utils import TipoPostagemEnum, SituacaoPostagemEnum
from src.Entidades.Postagem import Postagem
from src.Utils.Logger import Logger
from src.Servico import NotificacaoServico

log = Logger('PostagemServico')


def criar_postagem(postagem_json):
    validar_postagem_json(postagem_json)
    postagem = Postagem()
    postagem.definir_por_json(postagem_json)
    if postagem.tipo == TipoPostagemEnum.RESPOSTA:
        postagem_respondida = __responder_postagem(postagem.postagem_respondida_id)
        if postagem_respondida is not None and postagem_respondida.id != 0:
            NotificacaoServico.notificar_resposta_de_postagem(postagem_respondida, postagem)
    # TODO: Implementar Tema (categoria da postagem)
    return __criar_ou_atualizar(postagem)


def validar_postagem_json(postagem_json):
    if 'titulo' not in postagem_json:
        raise Exception("O Titulo da postagem não foi preenchido")
    if 'tipo' not in postagem_json:
        raise Exception("O Tipo da postagem não foi inserido!")
    if (postagem_json['tipo'] != TipoPostagemEnum.PERGUNTA) \
            and (postagem_json['tipo'] != TipoPostagemEnum.RESPOSTA):
        raise Exception("O Tipo da postagem não é válido! "
                        "Insira \'" + TipoPostagemEnum.PERGUNTA + "\' ou \'" + TipoPostagemEnum.RESPOSTA + "\'")
    if 'usuarioId' not in postagem_json:
        raise Exception("A ID do usuário não foi inseida!")


def pesquisar_postagens(pesquisa):
    postagem_repositorio = PostagemRepositorio()
    tuplas = postagem_repositorio.pesquisar_postagens_por_texto(pesquisa)
    return __lista_tuplas_para_lista_json(tuplas)


def __lista_tuplas_para_lista_json(tuplas):
    lista_postagem = ''
    if len(tuplas) > 1:
        lista_postagem += '[\n'
    for tupla in tuplas:
        postagem = Postagem()
        postagem.definir_por_tupla(tupla)
        lista_postagem += postagem.json_string()
        if tuplas.index(tupla) != (len(tuplas) - 1):
            lista_postagem += '\t,\n'
    if len(tuplas) > 1:
        lista_postagem += ']'
    return json.loads(lista_postagem)


# funções que começam com '__' são privadas (em teoria).
def __responder_postagem(postagem_respondida_id):
    try:
        log.info('Respondendo postagem ID: ' + str(postagem_respondida_id))
        postagem_repositorio = PostagemRepositorio()
        tupla = postagem_repositorio.buscar_por_id(postagem_respondida_id)
        postagem_respondida = Postagem()
        postagem_respondida.definir_por_tupla(tupla)
        postagem_respondida.situacao = SituacaoPostagemEnum.RESPONDIDA
        id_postagem_criada = __criar_ou_atualizar(postagem_respondida)
        postagem_respondida.id = id_postagem_criada
        return postagem_respondida
    except Exception as erro:
        log.erro('Erro ao responder a postagem ID: ' + str(postagem_respondida_id), erro)


def __criar_ou_atualizar(postagem):
    postagem_repositorio = PostagemRepositorio()
    ja_existe = postagem_repositorio.buscar_por_id(postagem.id) is not None
    if postagem.id is None or not ja_existe:
        return postagem_repositorio.criar(postagem)
    else:
        return postagem_repositorio.atualizar(postagem)
