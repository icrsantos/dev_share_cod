import smtplib
import ssl

from src.Utils.Logger import Logger
from src.Repositorio.UsuarioRepositorio import UsuarioRepositorio
from src.Entidades.Usuario import Usuario

log = Logger('NotificacaoServico')

servidor_smtp = "smtp.gmail.com"
porta = 587  # Para o starttls
email_remetente = "devsharenotif@gmail.com"
senha = 'sinistro_email2021'

# Criar contexto SSL seguro
contexto = ssl.create_default_context()


def __criar_servidor_conexao():
    try:
        servidor = smtplib.SMTP(servidor_smtp, porta)
        servidor.starttls(context=contexto)  # Estabelecer conexão
        servidor.login(email_remetente, senha)
        return servidor
    except Exception as erro:
        log.erro('Erro ao criar conexão com o servidor de e-mails da DevShare', erro)


def notificar_resposta_de_postagem(postagem_respondida):
    try:
        usuario_repositorio = UsuarioRepositorio()
        tupla = usuario_repositorio.buscar_por_id(postagem_respondida.usuario_id)
        usuario = Usuario()
        usuario.definir_por_tupla(tupla)
        enviar_email(usuario.email, 'teste')
    except Exception as erro:
        log.erro('Erro ao notiricar postagem ID: ' + postagem_respondida.id, erro)


def enviar_email(email_destinatario, mensagem):
    servidor = None
    try:
        servidor = __criar_servidor_conexao()
        servidor.sendmail(email_remetente, email_destinatario, mensagem)
        servidor.close()
        return True
    except Exception as erro:
        log.erro('Erro ao enviar e-mail para o destinatário \"' + email_destinatario + "\"", erro)
        servidor.close()
        return False
