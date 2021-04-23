import json
import smtplib
import ssl

from src.Entidades.Notificacao import Notificacao
from src.Repositorio.NotificacaoRepositorio import NotificacaoRepositorio
from src.Utils.Logger import Logger
from src.Repositorio.UsuarioRepositorio import UsuarioRepositorio
from src.Entidades.Usuario import Usuario

log = Logger('NotificacaoServico')

email_remetente = "devsharenotif@gmail.com"

# Criar contexto SSL seguro
contexto = ssl.create_default_context()


def __criar_servidor_conexao():
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls(context=contexto)  # Estabelecer conexão
        servidor.login("devsharenotif@gmail.com", 'sinistro_email2021')
        return servidor
    except Exception as erro:
        log.erro('Erro ao criar conexão com o servidor de e-mails da DevShare', erro)


def notificar_resposta_de_postagem(postagem_respondida, resposta_postagem):
    try:
        mensagem = __compor_mensagem_postagem_respondida(postagem_respondida, resposta_postagem)

        notificacao = Notificacao()
        notificacao.nova_notificacao = 'S'
        notificacao.postagem_id = postagem_respondida.id
        notificacao.tipo = 'RESPOSTA'
        notificacao.usuario_notificado_id = postagem_respondida.usuario_id
        notificacao.mensagem_enviada = mensagem

        notificacao_repositorio = NotificacaoRepositorio()
        notificacao_repositorio.salvar_notificacao(notificacao)

        __enviar_notificacao_autor(postagem_respondida, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar postagem ID: ' + postagem_respondida.id, erro)


def __compor_mensagem_postagem_respondida(postagem_respondida, resposta_postagem):
    mensagem = "Subject: Postagem respondida\n\n " \
               "A postagem \"" + postagem_respondida.titulo + "\" foi respondida! Eis a resposta:\n" \
               "\"" + resposta_postagem.conteudo + "\"\n"
    return mensagem


def __enviar_notificacao_autor(postagem_respondida, mensagem):
    try:
        usuario_repositorio = UsuarioRepositorio()
        tupla = usuario_repositorio.buscar_por_id(postagem_respondida.usuario_id)
        usuario = Usuario()
        usuario.definir_por_tupla(tupla)
        enviar_email(usuario.email, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar autor da postagem ID: ' + postagem_respondida.id, erro)


def enviar_email(email_destinatario, mensagem):
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