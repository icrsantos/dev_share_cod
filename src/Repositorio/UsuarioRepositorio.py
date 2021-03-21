import mysql.connector
from mysql.connector import errorcode


class UsuarioRepositorio:
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(host="localhost",
                                                   user="springuser",
                                                   password="sinistro",
                                                   port=3306,
                                                   database="dev_share"
                                                   )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro na validação! Confira o usuário e senha!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não encontrado!")
            else:
                print(err)

    def criar_usuario(self, usuario):
        try:
            mycursor = self.conexao.cursor()
            sql = "INSERT INTO usuario (nome, email, senha) " \
                  "VALUES (%s, %s, %s)"
            val = (usuario.nome, usuario.email, usuario.senha)
            mycursor.execute(sql, val)
            self.conexao.commit()
            self.conexao.close()
            return str(mycursor.lastrowid)
        except:
            print('Erro ao inserir cliente: ' + str(usuario))
            return 0
