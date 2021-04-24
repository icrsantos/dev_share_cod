from src.BancoDeDados.CriadorConexao import CriadorConexao
from src.Utils.Logger import Logger


class UsuarioRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('UsuarioRepositorio')
        self.criador_conexao = CriadorConexao()

    def salvar(self, usuario):
        try:
            self.log.info('Criando o usuario: ' + usuario.nome)
            executor = self.criador_conexao.criar_executor()
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
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Criado o usuario ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir usuario', erro)
            return str(0)

    def validar(self, nome, senha):
        try:
            self.log.info('Validando usuario ' + nome)
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT count(*) " \
                  "FROM usuario " \
                  "WHERE nome = %s " \
                  "AND senha = %s "
            parametros = (nome, senha)
            executor.execute(sql, parametros)
            resultado = executor.fetchone()
            self.criador_conexao.fechar_executor()
            self.log.info('Usuario ' + nome + ' validado: ' + str(resultado[0] == 1))
            return resultado[0] == 1
        except Exception as erro:
            self.log.erro('Erro ao validar usuario', erro)
            return False

    def buscar_por_id(self, usuario_id):
        try:
            self.log.info('Buscando usuario ID: ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * " \
                  "FROM usuario " \
                  "WHERE id = %s "
            executor.execute(sql, (usuario_id,))
            resultado = executor.fetchone()
            self.criador_conexao.fechar_executor()
            return resultado
        except Exception as erro:
            self.log.erro('Erro ao buscar usuario ID: ' + str(usuario_id), erro)
            return None

    def buscar_por_nome_usuario(self, nome_usuario):
        try:
            self.log.info('Buscando usuario name: ' + str(nome_usuario))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * " \
                  "FROM usuario " \
                  "WHERE nome = %s"
            executor.execute(sql, (nome_usuario,))
            resultado = executor.fetchone()
            self.criador_conexao.fechar_executor()
            return resultado
        except Exception as erro:
            self.log.erro('Erro ao buscar usuario name: ' + str(nome_usuario), erro)
            return None

    def editar(self, usuario):
        try:
            self.log.info('Editando o usuario: ' + usuario.nome)
            executor = self.criador_conexao.criar_executor()
            sql = "UPDATE usuario SET " \
                  "nome = %s," \
                  "email = %s," \
                  "data_alteracao = sysdate()" \
                  "WHERE id = %s"
            parametros = (
                usuario.nome,
                usuario.email,
                usuario.id
            )
            executor.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            self.log.info('Editado o usuario ID: ' + str(usuario.id))
            return str(usuario.id)
        except Exception as erro:
            self.log.erro('Erro ao editar o usuario', erro)
            return str(0)