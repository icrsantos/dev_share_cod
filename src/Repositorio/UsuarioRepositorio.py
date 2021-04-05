from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger


class UsuarioRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('UsuarioRepositorio')
        self.conexao = None

    def __criar_executor(self):
        self.conexao = CriadorConexao.criar_conexao()
        return self.conexao.cursor()

    def __commit_mudancas(self):
        self.conexao.commit()

    def __fechar_executor(self):
        self.conexao.close()

    def salvar(self, usuario):
        try:
            self.log.info('Criando o usuario: ' + usuario.nome)
            executor = self.__criar_executor()
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
            executor.execute(sql, parametros)
            self.__commit_mudancas()
            self.__fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Criado o usuario ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir usuario', erro)
            return str(0)

    def validar(self, nome, senha):
        try:
            self.log.info('Validando usuario ' + nome)
            executor = self.__criar_executor()
            sql = "SELECT count(*) " \
                  "FROM usuario " \
                  "WHERE nome = %s " \
                  "AND senha = %s "
            parametros = (nome, senha)
            executor.execute(sql, parametros)
            resultado = executor.fetchone()
            self.__fechar_executor()
            self.log.info('Usuario ' + nome + ' validado: ' + str(resultado[0] == 1))
            return resultado[0] == 1
        except Exception as erro:
            self.log.erro('Erro ao validar usuario', erro)
            return False

    def buscar_por_id(self, usuario_id):
        try:
            self.log.info('Buscando usuario ID: ' + str(usuario_id))
            executor = self.__criar_executor()
            sql = "SELECT * " \
                  "FROM usuario " \
                  "WHERE id = %s "
            executor.execute(sql, (usuario_id,))
            resultado = executor.fetchone()
            self.__fechar_executor()
            return resultado
        except Exception as erro:
            self.log.erro('Erro ao buscar usuario ID: ' + str(usuario_id), erro)
            return None
