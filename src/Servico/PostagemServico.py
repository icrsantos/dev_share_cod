from src.Repositorio.PostagemRepositorio import PostagemRepositorio
from src.Entidades.Postagem import Postagem
from src.Utils import TipoPostagemEnum, SituacaoPostagemEnum
from src.Entidades.Postagem import ListaPostagensDTO


def criar_postagem(postagem_json):
    validar_postagem_json(postagem_json)
    postagem = Postagem()
    postagem.definir_por_json(postagem_json)
    # TODO: Implementar Tema (categoria da postagem)
    postagem_repositorio = PostagemRepositorio()
    return postagem_repositorio.criar(postagem)


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
    tuplas = postagem_repositorio.buscar_postagens(pesquisa)
    return ListaPostagensDTO(tuplas).json()

