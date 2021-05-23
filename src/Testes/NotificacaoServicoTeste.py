import unittest

from src.Servico import NotificacaoServico, PostagemServico, UsuarioServico


class NotificacaoServicoTeste(unittest.TestCase):

    def testar_disparo_email_simples(self):
        email_destinatario = 'philemon.silva@gmail.com'
        mensagem = "Subject: Teste Unitário DevShare\n\n" \
                   "Essa é uma mensagem de teste proveniênte do teste unitário da Devshare"
        resultado = NotificacaoServico.__enviar_email(email_destinatario, mensagem)
        self.assertEqual(True, resultado)

    def testar_disparo_email_resposta(self):
        postagem_respondida = PostagemServico.buscar_postagem_por_id(22)
        postagem_resposta = PostagemServico.buscar_postagem_por_id(25)
        NotificacaoServico.notificar_resposta_de_postagem(postagem_respondida, postagem_resposta)
        self.assertEqual("OK", "OK")

    def testar_disparo_email_eco(self):
        usuario_ecoador = UsuarioServico.buscar_por_id(15)
        postagem_ecoada = PostagemServico.buscar_postagem_por_id(22)
        NotificacaoServico.notificar_eco_de_postagem(usuario_ecoador, postagem_ecoada)
        self.assertEqual("OK", "OK")


if __name__ == '__main__':
    unittest.main()
