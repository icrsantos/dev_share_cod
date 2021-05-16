from src.Entidades.Curtida import Curtida
from src.Repositorio.CurtidasRepositorio import CurtidasRepositorio
from src.Servico import PostagemServico


def postagem_ja_curtida_por_usuario(usuario_id, postagem_id):
    curtidas_repositorio = CurtidasRepositorio()

    curtida = Curtida()
    tupla = curtidas_repositorio.buscar(usuario_id, postagem_id)

    if tupla is not None:
        curtida.definir_por_tupla(tupla)
        return curtida.operacao
    else:
        return False


def curtir_postagem(usuario_id, postagem_id, like):
    curtidas_repositorio = CurtidasRepositorio()
    curtida = Curtida()
    curtida.postagem_id = postagem_id
    curtida.usuario_id = usuario_id
    if like:
        curtida.operacao = 'LIKE'
        __incrementar_curtidas_postagem(postagem_id)
    else:
        curtida.operacao = 'DISLIKE'
        __decrementar_curtidas_postagem(postagem_id)

    return curtidas_repositorio.criar(curtida)


def __incrementar_curtidas_postagem(postagem_id):
    postagem = PostagemServico.buscar_postagem_por_id(postagem_id)
    postagem.relevancia = postagem.relevancia + 1
    postagem.curtidas = postagem.curtidas + 1
    PostagemServico.criar_ou_atualizar(postagem)


def __decrementar_curtidas_postagem(postagem_id):
    postagem = PostagemServico.buscar_postagem_por_id(postagem_id)
    postagem.relevancia = postagem.relevancia - 1
    postagem.curtidas = postagem.curtidas - 1
    PostagemServico.criar_ou_atualizar(postagem)


def remover_curtida_usuario(usuario_id, postagem_id):
    curtidas_repositorio = CurtidasRepositorio()
    tupla = curtidas_repositorio.buscar(usuario_id, postagem_id)
    curtida = Curtida()
    curtida.definir_por_tupla(tupla)
    if curtida.operacao == 'LIKE':
        __decrementar_curtidas_postagem(postagem_id)
    else:
        __incrementar_curtidas_postagem(postagem_id)
    return curtidas_repositorio.remover(curtida)

