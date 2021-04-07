import unittest

from src.Servico import NotificacaoServico


class NotificacaoServicoTeste(unittest.TestCase):

    def testar_disparo_email_simples(self):
        email_destinatario = 'philemon.silva@gmail.com'
        mensagem = "Subject: Teste Unitário DevShare\n\n" \
                   "Essa é uma mensagem de teste proveniênte do teste unitário da Devshare"
        resultado = NotificacaoServico.enviar_email(email_destinatario, mensagem)
        self.assertEqual(True, resultado)


if __name__ == '__main__':
    unittest.main()
