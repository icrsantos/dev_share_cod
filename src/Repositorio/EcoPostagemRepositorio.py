from src.BancoDeDados.CriadorConexao import CriadorConexao
from src.Utils.Logger import Logger


class EcoPostagemRepositorio:
    def __init__(self):  # Construtora:
        self.log = Logger('EcoPostagemRepositorio')
        self.criador_conexao = CriadorConexao()

    def buscar(self, usuario_id, postagem_id):
        try:
            self.log.info('Buscando ecos de postagem ' + str(postagem_id) + ' de usuário ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * " \
                  "FROM ecos_postagem " \
                  "WHERE usuario_id = %s " \
                  "AND postagem_id = %s"
            parametros = (usuario_id, postagem_id)
            executor.execute(sql, parametros)
            tupla = executor.fetchone()
            return tupla
        except Exception as erro:
            self.log.erro('Erro ao buscar ecos de usuário ' + str(usuario_id)
                          + ' para postagem  ' + str(postagem_id), erro)
            return None

    def salvar(self, eco):
        try:
            self.log.info('Inserindo notificação')
            executor_notificacao = self.criador_conexao.criar_executor()
            sql = "INSERT INTO ecos_postagem" \
                  "(data_insercao, data_alteracao," \
                  "usuario_id, postagem_id) " \
                  "VALUES (%s, %s, %s, %s)"
            parametros = (
                eco.data_insercao,
                eco.data_alteracao,
                eco.usuario_id,
                eco.postagem_id
            )
            executor_notificacao.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            id_eco = str(executor_notificacao.lastrowid)
            self.log.info('Criado o eco ID: ' + id_eco)
        except Exception as erro:
            self.log.erro('Erro ao inserir eco de usuario ' + str(eco.usuario_id) +
                          ' em postagem ' + str(eco.postagem_id), erro)
            return str(0)

    def remover(self, eco):
        try:
            self.log.info('Removendo eco de Usuario ' + str(eco.usuario_id)
                          + " na postagem " + str(eco.postagem_id))
            executor = self.criador_conexao.criar_executor()
            sql = "DELETE FROM ecos_postagem " \
                  "WHERE (usuario_id = %s) " \
                  " AND (postagem_id = %s)  "
            parametros = (
                eco.usuario_id,
                eco.postagem_id
            )
            executor.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            self.log.info('Eco de Usuario ' + str(eco.usuario_id)
                          + " na postagem " + str(eco.postagem_id) + " Removido com sucesso")
            return True
        except Exception as erro:
            self.log.erro('Falha de Usuario ' + str(eco.usuario_id) + " ao remover eco da postagem "
                          + str(eco.postagem_id), erro)
            return False

    def buscar_por_postagem_id(self, postagem_id):
        try:
            self.log.info('Buscando ecos de postagem ' + str(postagem_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * " \
                  "FROM ecos_postagem " \
                  "WHERE postagem_id = %s "
            executor.execute(sql, (postagem_id,))
            tuplas = executor.fetchall()
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar ecos para postagem  ' + str(postagem_id), erro)
            return None
