import mysql.connector
from mysql.connector import errorcode

conexao = None


def __criar_conexao():
    try:
        return mysql.connector.connect(host="localhost",
                                       user="springuser",
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


def criar_executor():
    global conexao
    conexao = __criar_conexao()
    return conexao.cursor()


def commit_mudancas():
    conexao.commit()


def fechar_executor():
    conexao.close()
