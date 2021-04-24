from src.BancoDeDados.CriadorConexao import CriadorConexao
from src.Utils.Logger import Logger


class NotificacaoRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('NotificacaoRepositorio')
        self.criador_conexao = CriadorConexao()

    def novas_notificacoes(self, usuario_id):
        try:
            self.log.info('Buscando novas notificações do usuário ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT count(*) " \
                  "FROM historico_notificacoes " \
                  "WHERE usuario_notificado_id = %s " \
                  "AND nova_notificacao = %s"
            executor.execute(sql, (usuario_id, 'S',))
            tupla_novas_notificacao = executor.fetchone()
            self.criador_conexao.fechar_executor()
            self.log.info(str(tupla_novas_notificacao[0]) + ' notificações novas encontradas para o usuário ' + str(usuario_id))
            return str(tupla_novas_notificacao[0])
        except Exception as erro:
            self.log.erro('Erro ao buscar novas notificações do usuário ' + str(usuario_id), erro)
            return str(0)

    def buscar_notificacoes(self, usuario_id):
        try:
            self.log.info('Buscando notificações do usuário ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * " \
                  "FROM historico_notificacoes " \
                  "WHERE usuario_notificado_id = %s " \
                  "ORDER BY data_insercao desc"
            executor.execute(sql, (usuario_id,))
            tupla_notificacao = executor.fetchall()
            self.criador_conexao.fechar_executor()
            self.log.info(str(len(tupla_notificacao)) + ' notificações encontradas para o usuário ' + str(usuario_id))
            return tupla_notificacao
        except Exception as erro:
            self.log.erro('Erro ao buscar as notificações do usuário ' + str(usuario_id), erro)
            return str(0)

    def limpar_notificacoes(self, usuario_id):
        try:
            self.log.info('Limpando notificações do usuário ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "UPDATE historico_notificacoes " \
                  "SET nova_notificacao = %s " \
                  "WHERE usuario_notificado_id = %s " \
                  "AND data_insercao < sysdate()"
            executor.execute(sql, ('N', usuario_id))
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            self.log.info('Notificações limpas para o usuário ' + str(usuario_id))
        except Exception as erro:
            self.log.erro('Erro ao limpar as notificações do usuário ' + str(usuario_id), erro)
            return str(0)

    def salvar_notificacao(self, notificacao):
        try:
            self.log.info('Inserindo notificação')
            executor_notificacao = self.criador_conexao.criar_executor()
            sql = "INSERT INTO historico_notificacoes" \
                  "(data_insercao, data_alteracao," \
                  "usuario_notificado_id, postagem_id," \
                  "mensagem_enviada, nova_notificacao, tipo) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            parametros = (
                notificacao.data_insercao,
                notificacao.data_alteracao,
                notificacao.usuario_notificado_id,
                notificacao.postagem_id,
                notificacao.mensagem_enviada,
                notificacao.nova_notificacao,
                notificacao.tipo
            )
            executor_notificacao.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            id_notificacao = str(executor_notificacao.lastrowid)
            self.log.info('Criada a notificação ID: ' + id_notificacao)
        except Exception as erro:
            self.log.erro('Erro ao inserir uma notificação para o usuário' + str(notificacao.usuario_notificado_id), erro)
            return str(0)