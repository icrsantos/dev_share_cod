import mysql.connector
from mysql.connector import errorcode


class CriadorConexao():
    def __init__(self):
        self.conexao = None

    def __criar_conexao(self):
        try:
            self.conexao = mysql.connector.connect(host="devshare.mysql.database.azure.com",
                                                   user="devshareuser@devshare.mysql.database.azure.com",
                                                   password="sinistro",
                                                   port=3306,
                                                   database="dev_share"
                                                   )
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro na validação! Confira o usuário e senha!")
            elif erro.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não encontrado!")
            else:
                print(erro)
            return None

    def criar_executor(self):
        self.__criar_conexao()
        return self.conexao.cursor()

    def commit_mudancas(self):
        if self.conexao is None:
            self.criar_executor()
        self.conexao.commit()

    def fechar_executor(self):
        if self.conexao is None:
            self.criar_executor()
        self.conexao.close()
