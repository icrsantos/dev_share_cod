import datetime

from src.BancoDeDados.CriadorConexao import CriadorConexao
from src.Utils.Logger import Logger


class CurtidasRepositorio:
    def __init__(self):
        self.log = Logger('CurtidasRepositorio')
        self.criador_conexao = CriadorConexao()

    def criar(self, usuario_id, postagem_id):
        try:
            self.log.info('Inserindo novo registro de curtida')
            executor = self.criador_conexao.criar_executor()
            sql = "INSERT INTO curtidas" \
                  "(data_insercao, data_alteracao," \
                  "usuario_id, postagem_id) " \
                  "VALUES (%s, %s, %s, %s)"
            parametros = (
                datetime.datetime.now(),
                datetime.datetime.now(),
                usuario_id,
                postagem_id
            )
            executor.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Usuario ' + usuario_id + " curtiu a postagem " + postagem_id)
            return id_criacao
        except Exception as erro:
            self.log.erro('Falha de Usuario ' + usuario_id + " ao curtir a postagem " + postagem_id, erro)
            return str(0)
