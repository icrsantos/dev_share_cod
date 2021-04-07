import smtplib
import ssl

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
        __enviar_notificacao_autor(postagem_respondida, mensagem)
    except Exception as erro:
        log.erro('Erro ao notificar postagem ID: ' + postagem_respondida.id, erro)


def __compor_mensagem_postagem_respondida(postagem_respondida, resposta_postagem):
    mensagem = "Subject: Postagem respondida\n\n " \
               "A postagem \"" + postagem_respondida.titulo + "\" foi respondida! Eis a resposta:\n" \
               "\"" + resposta_postagem.conteudo + "\n"
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
