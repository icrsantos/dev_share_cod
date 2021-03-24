from src.BancoDeDados import CriadorConexao
from src.Utils import Logger


class UsuarioRepositorio:
    def __init__(self):  # Construtora:
        self.nome_classe = 'UsuarioRepositorio'
        self.conexao = None

    def salvar(self, usuario):
        try:
            Logger.info('Validando usuario ' + usuario.nome, self.nome_classe)
            self.conexao = CriadorConexao.criar_conexao()
            mycursor = self.conexao.cursor()
            sql = "INSERT INTO usuario " \
                  "(data_insercao, data_alteracao, nome, email, senha) " \
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
            id_criacao = str(mycursor.lastrowid)
            Logger.info('Criado o usuario ID: ' + id_criacao, self.nome_classe)
            return id_criacao
        except Exception as erro:
            Logger.erro('Erro ao inserir usuario', erro, self.nome_classe)
            return str(0)

    def validar(self, nome, senha):
        try:
            Logger.info('Validando usuario ' + nome, self.nome_classe)
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
            Logger.info('Usuario ' + nome + ' validado: ' + str(resultado[0] == 1), self.nome_classe)
            return resultado[0] == 1
        except Exception as erro:
            Logger.erro('Erro ao validar usuario', erro, self.nome_classe)
            return False
