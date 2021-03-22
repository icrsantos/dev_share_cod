import mysql.connector
from mysql.connector import errorcode


class UsuarioRepositorio:
    def __init__(self):  # Construtora:
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

    def salvar(self, usuario):
        try:
            mycursor = self.conexao.cursor()
            sql = "INSERT INTO usuario (data_insercao, data_alteracao, nome, email, senha) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            parametros = (
                usuario.data_insercao,
                usuario.data_alteracao,
                usuario.nome,
                usuario.email,
                usuario.senha
            )
            mycursor.execute(sql, parametros)
            self.conexao.commit()
            self.conexao.close()
            return str(mycursor.lastrowid)
        except:
            print('Erro ao inserir cliente: ' + str(usuario))
            return 0
