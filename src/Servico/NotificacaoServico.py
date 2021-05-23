import json
import smtplib
import ssl

from src.Entidades.Notificacao import Notificacao
from src.Repositorio.NotificacaoRepositorio import NotificacaoRepositorio
from src.Utils.Logger import Logger
from src.Utils import TipoNotificacaoEnum
from src.Servico import EcoPostagemServico, UsuarioServico

log = Logger('NotificacaoServico')

email_remetente = "devsharenotif@gmail.com"
senha = 'sinistro_email2021'

# Criar contexto SSL seguro
contexto = ssl.create_default_context()


def __criar_servidor_conexao():
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls(context=contexto)  # Estabelecer conexão
        servidor.login(email_remetente, senha)
        return servidor
    except Exception as erro:
        log.erro('Erro ao criar conexão com o servidor de e-mails da DevShare', erro)


def notificar_resposta_de_postagem(postagem_respondida, postagem_resposta):
    try:
        mensagem = __compor_mensagem_postagem_respondida(postagem_respondida, postagem_resposta)
        __criar_notificacao(
            postagem_respondida,
            TipoNotificacaoEnum.RESPOSTA,
            "A postagem " + postagem_respondida.titulo + " foi respondida!"
        )
        __enviar_notificacao_autor(postagem_respondida, mensagem)
        __enviar_notificacao_usuarios_que_ecoam_postagem(postagem_respondida, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar resposta de postagem ID: ' + postagem_respondida.id, erro)


def __compor_mensagem_postagem_respondida(postagem_respondida, resposta_postagem):
    mensagem = "Subject: Postagem respondida\n\n " \
               "A postagem \"" + postagem_respondida.titulo + "\" foi respondida! Eis a resposta:\n" \
               "\"" + resposta_postagem.conteudo + "\"\n"
    return mensagem


def __enviar_notificacao_autor(postagem, mensagem):
    try:
        usuario = UsuarioServico.buscar_por_id(postagem.usuario_id)
        __enviar_email(usuario.email, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar autor da postagem ID: ' + postagem.id, erro)


def __enviar_email(email_destinatario, mensagem):
    servidor = None
    try:
        servidor = __criar_servidor_conexao()
        servidor.sendmail(email_remetente, email_destinatario, mensagem.encode('utf-8'))
        servidor.close()
        return True
    except Exception as erro:
        log.erro('Erro ao enviar e-mail para o destinatário \"' + email_destinatario + "\"", erro)
        servidor.close()
        return False


def notificar_eco_de_postagem(usuario_ecoador, postagem_ecoada):
    try:
        mensagem = __compor_mensagem_postagem_ecoada(postagem_ecoada, usuario_ecoador)
        __criar_notificacao(
            postagem_ecoada,
            TipoNotificacaoEnum.ECO,
            "A postagem " + postagem_ecoada.titulo + " foi ecoada por " + usuario_ecoador.nome + "!"
        )
        __enviar_notificacao_autor(postagem_ecoada, mensagem)
        __enviar_notificacao_usuarios_que_ecoam_postagem(postagem_ecoada, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar eco de postagem ID: ' + postagem_ecoada.id, erro)


def __compor_mensagem_postagem_ecoada(postagem_ecoada, usuario_ecoador):
    mensagem = "Subject: Postagem Ecoada!\n\n " \
               "A postagem \"" + postagem_ecoada.titulo + "\"" \
               " foi ecoada pelo usuário \"" + usuario_ecoador.nome + "\"!\n" + \
               " Caso já saiba a resposta da postagem, contate-o no e-mail \"" + usuario_ecoador.email + "\""
    return mensagem


def __enviar_notificacao_usuarios_que_ecoam_postagem(postagem_ecoada, mensagem):
    try:
        ecos = EcoPostagemServico.buscar_ecos_por_postagem_id(postagem_ecoada.id)
        for eco in ecos:
            usuario = UsuarioServico.buscar_por_id(eco.usuario_id)
            __enviar_email(usuario.email, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar usuarios que ecoaram a postagem ID: ' + postagem_ecoada.id, erro)


def novas_notificacoes(usuario_id):
    notificacao_repositorio = NotificacaoRepositorio()
    return notificacao_repositorio.novas_notificacoes(usuario_id)


def buscar_notificacoes(usuario_id):
    notificacao_repositorio = NotificacaoRepositorio()
    tuplas = notificacao_repositorio.buscar_notificacoes(usuario_id)
    return __lista_tuplas_para_lista_json(tuplas)


def limpar_notificacoes(usuario_id):
    notificacao_repositorio = NotificacaoRepositorio()
    notificacao_repositorio.limpar_notificacoes(usuario_id)
    return buscar_notificacoes(usuario_id)


def __criar_notificacao(postagem, tipo, titulo):
    notificacao = Notificacao()
    notificacao.nova_notificacao = 'S'
    notificacao.postagem_id = postagem.id
    notificacao.tipo = tipo
    notificacao.usuario_notificado_id = postagem.usuario_id
    notificacao.mensagem_enviada = titulo
    notificacao_repositorio = NotificacaoRepositorio()
    return notificacao_repositorio.salvar_notificacao(notificacao)


def __lista_tuplas_para_lista_json(tuplas):
    lista_notificacoes = ''
    if len(tuplas) == 0:
        return []
    if len(tuplas) >= 1:
        lista_notificacoes += '[\n'
    for tupla in tuplas:
        notificacao = Notificacao()
        notificacao.definir_por_tupla(tupla)
        lista_notificacoes += notificacao.json_string()
        if tuplas.index(tupla) != (len(tuplas) - 1):
            lista_notificacoes += '\t,\n'
    if len(tuplas) >= 1:
        lista_notificacoes += ']'
    return json.loads(lista_notificacoes)
