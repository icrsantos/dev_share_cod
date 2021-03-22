from src.BancoDeDados import CriadorConexao


class UsuarioRepositorio:
    def __init__(self):  # Construtora:
        self.conexao = None

    def salvar(self, usuario):
        try:
            self.conexao = CriadorConexao.criar_conexao()
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
        except Exception as erro:
            print('Erro ao inserir cliente: ' + str(erro))
            return str(0)

    def validar(self, nome, senha):
        try:
            self.conexao = CriadorConexao.criar_conexao()
            mycursor = self.conexao.cursor()
            sql = "SELECT count(*) " \
                  "FROM usuario " \
                  "WHERE nome = %s " \
                  "AND senha = %s "
            parametros = (nome, senha)
            mycursor.execute(sql, parametros)
            resultado = mycursor.fetchone()
            self.conexao.close()
            return resultado[0] == 1
        except Exception as erro:
            print('Erro ao inserir cliente: ' + str(erro))
            return False
