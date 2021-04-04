from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger
from src.Utils import TipoPostagemEnum


class PostagemRepositorio:
    def __init__(self):  # Construtora:
        self.conexao = None
        self.log = Logger('PostagemRepositorio')

    def __criar_executor(self):
        self.conexao = CriadorConexao.criar_conexao()
        return self.conexao.cursor()

    def __commit_mudancas(self):
        self.conexao.commit()

    def __fechar_executor(self):
        self.conexao.close()

    def criar(self, postagem):
        try:
            self.log.info('Inserindo nova postagem')
            executor = self.__criar_executor()
            sql = "INSERT INTO postagem" \
                  "(data_insercao, data_alteracao," \
                  "titulo, conteudo, tipo, situacao," \
                  "postagem_respondida_id, usuario_id) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            parametros = (
                postagem.data_insercao,
                postagem.data_alteracao,
                postagem.titulo,
                postagem.conteudo,
                postagem.tipo,
                postagem.situacao,
                postagem.postagem_respondida_id,
                postagem.usuario_id
            )
            executor.execute(sql, parametros)
            self.__commit_mudancas()
            self.__fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Criada a postagem ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir postagem', erro)
            return str(0)

    def atualizar(self, postagem):
        try:
            self.log.info('Atualizando postagem ID: ' + str(postagem.id))
            executor = self.__criar_executor()
            sql = "UPDATE postagem SET " \
                  "data_alteracao = %s, " \
                  "titulo = %s, conteudo = %s, tipo = %s, situacao = %s, " \
                  "postagem_respondida_id = %s, usuario_id = %s " \
                  "WHERE id = %s"
            parametros = (
                postagem.data_alteracao,
                postagem.titulo,
                postagem.conteudo,
                postagem.tipo,
                postagem.situacao,
                postagem.postagem_respondida_id,
                postagem.usuario_id,
                postagem.id
            )
            executor.execute(sql, parametros)
            self.__commit_mudancas()
            self.__fechar_executor()
            self.log.info('Atualizada a postagem ID: ' + str(postagem.id))
            return str(postagem.id)
        except Exception as erro:
            self.log.erro('Erro ao atualizar postagem ID: ' + str(postagem.id), erro)
            return str(0)

    def buscar_por_id(self, postagem_id):
        try:
            self.log.info('Conferindo existência de postagem ID: ' + str(postagem_id))
            executor = self.__criar_executor()
            sql = "SELECT * FROM postagem WHERE" \
                  "(id = %s) "
            executor.execute(sql, (postagem_id,))
            tupla = executor.fetchall()
            self.__fechar_executor()
            return tupla
        except Exception as erro:
            self.log.erro('Erro ao conferir existência da postagem ID: ' + str(postagem_id), erro)
            return None

    def pesquisar_postagens_por_texto(self, texto_pesquisa):
        try:
            self.log.info('Buscando posts com a mensagem \'' + texto_pesquisa + '\'')
            executor = self.__criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(titulo like '%" + texto_pesquisa + "%') OR " \
                  "(conteudo like '%" + texto_pesquisa + "%') OR " \
                  "(tipo like '%" + texto_pesquisa + "%')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            executor.execute(sql)
            tuplas = executor.fetchall()
            self.__fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar postagem', erro)
            return str('ERRO: ' + str(erro))

    def buscar_respostas_a_postagem(self, postagem_id):
        try:
            self.log.info('Buscando respostas ao post ID: ' + str(postagem_id))
            executor = self.__criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(postagem_respondida_id = %s ) AND " \
                  "(tipo = '" + TipoPostagemEnum.RESPOSTA + "')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            executor.execute(sql, (postagem_id,))
            tuplas = executor.fetchall()
            self.__fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar respostas da postagem ID: ' + str(postagem_id), erro)
            return str('ERRO: ' + str(erro))

