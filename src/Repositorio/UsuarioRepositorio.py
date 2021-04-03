from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger


class UsuarioRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('UsuarioRepositorio')
        self.conexao = None

    def salvar(self, usuario):
        try:
            self.log.info('Validando usuario ' + usuario.nome)
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
            self.log.info('Criado o usuario ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir usuario', erro)
            return str(0)

    def validar(self, nome, senha):
        try:
            self.log.info('Validando usuario ' + nome)
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
            self.log.info('Usuario ' + nome + ' validado: ' + str(resultado[0] == 1))
            return resultado[0] == 1
        except Exception as erro:
            self.log.erro('Erro ao validar usuario', erro)
            return False
