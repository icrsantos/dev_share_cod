import mysql.connector
from mysql.connector import errorcode


class PostagemRepositorio:
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

    def buscar_postagens(self, texto_pesquisa):
        try:
            mycursor = self.conexao.cursor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(titulo like '%%%s%%') OR" \
                  "(conteudo like '%%%s%%') OR" \
                  "(tipo_postagem like '%%%s%%')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            parametros = texto_pesquisa
            mycursor.execute(sql, parametros)
            resultados = mycursor.fetchall()
            self.conexao.close()
            return str(resultados)
        except:
            print('Erro ao buscar postagens')
            return []
