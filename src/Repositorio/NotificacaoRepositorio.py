from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger


class NotificacaoRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('NotificacaoRepositorio')
        self.conexao = None

    def __criar_executor(self):
        self.conexao = CriadorConexao.criar_conexao()
        return self.conexao.cursor()

    def __commit_mudancas(self):
        self.conexao.commit()

    def __fechar_executor(self):
        self.conexao.close()

    def novas_notificacoes(self, usuario_id):
        try:
            self.log.info('Buscando novas notificações do usuário ' + str(usuario_id))
            executor = self.__criar_executor()
            sql = "SELECT count(*) " \
                  "FROM historico_notificacoes " \
                  "WHERE usuario_notificado_id = %s " \
                  "AND nova_notificacao = %s"
            executor.execute(sql, (usuario_id, 'S'))
            resultado = executor.fetchone()
            self.__fechar_executor()
            self.log.info(str(resultado[0]) + ' notificações novas encontradas para o usuário ' + str(usuario_id))
            return str(resultado[0])
        except Exception as erro:
            self.log.erro('Erro ao buscar novas notificações do usuário ', str(usuario_id), erro)
            return str(0)

    def buscar_notificacoes(self, usuario_id):
        try:
            self.log.info('Buscando notificações do usuário ' + str(usuario_id))
            executor = self.__criar_executor()
            sql = "SELECT * " \
                  "FROM historico_notificacoes " \
                  "WHERE usuario_notificado_id = %s"
            executor.execute(sql, (usuario_id,))
            resultado = executor.fetchall()
            self.__fechar_executor()
            self.log.info(str(len(resultado)) + ' notificações encontradas para o usuário ' + str(usuario_id))
            return resultado
        except Exception as erro:
            self.log.erro('Erro ao buscar as notificações do usuário ' + str(usuario_id), erro)
            return str(0)