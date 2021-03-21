import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(host="localhost",
                                  user="springuser",
                                  password="sinistro",
                                  port=3306,
                                  database="dev_share"
                                  )
    mycursor = cnx.cursor()
    sql = "INSERT INTO usuario (email, nome, senha) " \
          "VALUES (%s, %s, %s)"
    val = ("John@teste.com", "john", "abc123")
    mycursor.execute(sql, val)
    cnx.commit()
    for x in mycursor:
        print(x)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro na validação! Confira o usuário e senha!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
