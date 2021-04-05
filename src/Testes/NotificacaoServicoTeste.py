import unittest

from src.Servico import NotificacaoServico


class NotificacaoServicoTeste(unittest.TestCase):

    def testar_disparo_email_simples(self):
        email_destinatario = 'philemon.silva@gmail.com'
        mensagem = """Subject: Hi there
        
        
        This message is sent from Python."""
        resultado = NotificacaoServico.enviar_email(email_destinatario, mensagem)
        self.assertEqual(True, resultado)

    def testar_disparo_notificacao_resposta(self):
        email_destinatario = 'philemon.silva@gmail.com'
        mensagem = """Subject: Hi there


        This message is sent from Python."""
        resultado = NotificacaoServico.enviar_email(email_destinatario, mensagem)
        self.assertEqual(True, resultado)


if __name__ == '__main__':
    unittest.main()
