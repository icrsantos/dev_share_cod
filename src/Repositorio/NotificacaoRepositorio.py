from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger


class NotificacaoRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('NotificacaoRepositorio')
        self.conexao = None

    def novas_notificacoes(self, usuario_id):
        try:
            self.log.info('Buscando novas notificações do usuário ' + str(usuario_id))
            executor = CriadorConexao.criar_executor()
            sql = "SELECT count(*) " \
                  "FROM historico_notificacoes " \
                  "WHERE usuario_notificado_id = %s " \
                  "AND nova_notificacao = %s"
            executor.execute(sql, (usuario_id, 'S'))
            resultado = executor.fetchone()
            CriadorConexao.fechar_executor()
            self.log.info(str(resultado[0]) + ' notificações novas encontradas para o usuário ' + str(usuario_id))
            return str(resultado[0])
        except Exception as erro:
            self.log.erro('Erro ao buscar novas notificações do usuário ', str(usuario_id), erro)
            return str(0)

    def buscar_notificacoes(self, usuario_id):
        try:
            self.log.info('Buscando notificações do usuário ' + str(usuario_id))
            executor = CriadorConexao.criar_executor()
            sql = "SELECT * " \
                  "FROM historico_notificacoes " \
                  "WHERE usuario_notificado_id = %s" \
                  "ORDER BY data_insercao desc"
            executor.execute(sql, (usuario_id,))
            resultado = executor.fetchall()
            CriadorConexao.fechar_executor()
            self.log.info(str(len(resultado)) + ' notificações encontradas para o usuário ' + str(usuario_id))
            return resultado
        except Exception as erro:
            self.log.erro('Erro ao buscar as notificações do usuário ' + str(usuario_id), erro)
            return str(0)

    def limpar_notificacoes(self, usuario_id):
        try:
            self.log.info('Limpando notificações do usuário ' + str(usuario_id))
            executor = CriadorConexao.criar_executor()
            sql = "UPDATE historico_notificacoes " \
                  "SET nova_notificacao = %s " \
                  "WHERE usuario_notificado_id = %s" \
                  "AND data_insercao < sysdate()"
            executor.execute(sql, ('N', usuario_id))
            CriadorConexao.commit_mudancas()
            CriadorConexao.fechar_executor()
            self.log.info('Notificações limpas para o usuário ' + str(usuario_id))
        except Exception as erro:
            self.log.erro('Erro ao limpar as notificações do usuário ' + str(usuario_id), erro)
            return str(0)