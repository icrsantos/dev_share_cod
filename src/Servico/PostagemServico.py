from src.Repositorio.PostagemRepositorio import PostagemRepositorio
from src.Entidades.Postagem import Postagem
from src.Utils import TipoPostagemEnum, SituacaoPostagemEnum
from src.Entidades.Postagem import PostagemDTO
from src.Utils.Logger import Logger

log = Logger('PostagemServico')


def criar_postagem(postagem_json):
    validar_postagem_json(postagem_json)
    postagem = Postagem()
    postagem.definir_por_json(postagem_json)
    if postagem.tipo == TipoPostagemEnum.RESPOSTA:
        __responder_postagem(postagem.postagem_respondida_id)
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
    return PostagemDTO(tuplas).json()


# funções que começam com '__' são privadas (em teoria).
def __responder_postagem(postagem_id):
    try:
        log.info('Respondendo postagem ID: ' + str(postagem_id))
        postagem_repositorio = PostagemRepositorio()
        tupla = postagem_repositorio.buscar_por_id(postagem_id)
        postagem_respondida = Postagem()
        postagem_respondida.definir_por_json(PostagemDTO(tupla).json())
        postagem_respondida.situacao = SituacaoPostagemEnum.RESPONDIDA
        __criar_ou_atualizar(postagem_respondida)
    except Exception as erro:
        log.erro('Erro ao responder a postagem ID: ' + str(postagem_id), erro)


def __criar_ou_atualizar(postagem):
    postagem_repositorio = PostagemRepositorio()
    ja_existe = len(postagem_repositorio.buscar_por_id(postagem.id)) == 1
    if postagem.id is None or not ja_existe:
        return postagem_repositorio.criar(postagem)
    else:
        return postagem_repositorio.atualizar(postagem)
