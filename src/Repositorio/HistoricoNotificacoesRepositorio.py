from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger
from src.Utils import TipoPostagemEnum


class HistoricoNotificacoesRepositorio:
    def __init__(self):
        self.conexao = None
        self.log = Logger('HistoricoNotificacoesRepositorio')
