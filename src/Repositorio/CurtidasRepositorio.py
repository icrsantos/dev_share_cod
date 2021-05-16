import datetime

from src.BancoDeDados.CriadorConexao import CriadorConexao
from src.Utils.Logger import Logger


class CurtidasRepositorio:
    def __init__(self):
        self.log = Logger('CurtidasRepositorio')
        self.criador_conexao = CriadorConexao()

    def criar(self, curtida):
        try:
            self.log.info('Inserindo novo registro de curtida')
            executor = self.criador_conexao.criar_executor()
            sql = "INSERT INTO curtidas" \
                  "(data_insercao, data_alteracao," \
                  "usuario_id, postagem_id, operacao) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            parametros = (
                datetime.datetime.now(),
                datetime.datetime.now(),
                curtida.usuario_id,
                curtida.postagem_id,
                curtida.operacao
            )
            executor.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Usuario ' + str(curtida.usuario_id) + " curtiu a postagem " + str(curtida.postagem_id))
            return id_criacao
        except Exception as erro:
            self.log.erro('Falha de Usuario ' + str(curtida.usuario_id) + " ao curtir a postagem " + str(curtida.postagem_id), erro)
            return str(0)

    def buscar(self, usuario_id, postagem_id):
        try:
            self.log.info('Buscand curtida de usuario ' + str(usuario_id) + "em postagem " + str(postagem_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * FROM curtidas WHERE" \
                  "(usuario_id = %s) AND (postagem_id = %s)"
            parametros = (
                usuario_id,
                postagem_id
            )
            executor.execute(sql, parametros)
            tupla = executor.fetchone()
            self.criador_conexao.fechar_executor()
            return tupla
        except Exception as erro:
            self.log.erro('Erro ao buscar a postagem ID: ' + str(postagem_id), erro)
            return None
