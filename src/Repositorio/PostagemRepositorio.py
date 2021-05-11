from src.Utils.Logger import Logger
from src.Utils import TipoPostagemEnum
from src.BancoDeDados.CriadorConexao import CriadorConexao


class PostagemRepositorio:
    def __init__(self):  # Construtora:
        self.criador_conexao = CriadorConexao()
        self.log = Logger('PostagemRepositorio')

    def criar(self, postagem):
        try:
            self.log.info('Inserindo nova postagem')
            executor = self.criador_conexao.criar_executor()
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
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Criada a postagem ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir postagem', erro)
            return str(0)

    def atualizar(self, postagem):
        try:
            self.log.info('Atualizando postagem ID: ' + str(postagem.id))
            executor = self.criador_conexao.criar_executor()
            sql = "UPDATE postagem SET " \
                  "data_alteracao = %s, " \
                  "titulo = %s, conteudo = %s, tipo = %s, situacao = %s," \
                  "curtidas = %s, relevancia = %s, " \
                  "postagem_respondida_id = %s, usuario_id = %s " \
                  "WHERE id = %s"
            parametros = (
                postagem.data_alteracao,
                postagem.titulo,
                postagem.conteudo,
                postagem.tipo,
                postagem.situacao,
                postagem.curtidas,
                postagem.relevancia,
                postagem.postagem_respondida_id,
                postagem.usuario_id,
                postagem.id
            )
            executor.execute(sql, parametros)
            self.criador_conexao.commit_mudancas()
            self.criador_conexao.fechar_executor()
            self.log.info('Atualizada a postagem ID: ' + str(postagem.id))
            return str(postagem.id)
        except Exception as erro:
            self.log.erro('Erro ao atualizar postagem ID: ' + str(postagem.id), erro)
            return str(0)

    def buscar_por_id(self, postagem_id):
        try:
            self.log.info('Buscando a postagem ID: ' + str(postagem_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * FROM postagem WHERE" \
                  "(id = %s) "
            executor.execute(sql, (postagem_id,))
            tupla = executor.fetchone()
            self.criador_conexao.fechar_executor()
            return tupla
        except Exception as erro:
            self.log.erro('Erro ao buscar a postagem ID: ' + str(postagem_id), erro)
            return None

    def pesquisar_postagens_por_texto(self, texto_pesquisa):
        try:
            self.log.info('Buscando posts com a mensagem \'' + texto_pesquisa + '\'')
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * FROM postagem WHERE " \
                  "(tipo = '" + TipoPostagemEnum.PERGUNTA + "') AND (" \
                  "(titulo like '%" + texto_pesquisa + "%') OR " \
                  "(conteudo like '%" + texto_pesquisa + "%') OR " \
                  "(tipo like '%" + texto_pesquisa + "%') " \
                  ")" \
                  "ORDER BY relevancia DESC "
            executor.execute(sql)
            tuplas = executor.fetchall()
            self.criador_conexao.fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar postagem', erro)
            return str('ERRO: ' + str(erro))

    def buscar_respostas_a_postagem(self, postagem_id):
        try:
            self.log.info('Buscando respostas ao post ID: ' + str(postagem_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(postagem_respondida_id = %s ) AND " \
                  "(tipo = '" + TipoPostagemEnum.RESPOSTA + "')" \
                  ")" \
                  "ORDER BY relevancia DESC "
            executor.execute(sql, (postagem_id,))
            tuplas = executor.fetchall()
            self.criador_conexao.fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar respostas da postagem ID: ' + str(postagem_id), erro)
            return str('ERRO: ' + str(erro))

    def buscar_perguntas_de_usuario(self, usuario_id):
        try:
            self.log.info('Buscando perguntas do usuario ID: ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(usuario_id = %s ) AND " \
                  "(tipo = '" + TipoPostagemEnum.PERGUNTA + "')" \
                  ")" \
                  "ORDER BY relevancia DESC "
            executor.execute(sql, (usuario_id,))
            tuplas_perguntas = executor.fetchall()
            self.criador_conexao.fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas_perguntas)) + ' resultados')
            return tuplas_perguntas
        except Exception as erro:
            self.log.erro('Erro ao buscar perguntas do usuario ID: ' + str(usuario_id), erro)
            return str('ERRO: ' + str(erro))

    def buscar_respostas_de_usuario(self, usuario_id):
        try:
            self.log.info('Buscando respostas do usuario ID: ' + str(usuario_id))
            executor = self.criador_conexao.criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(usuario_id = %s ) AND " \
                  "(tipo = '" + TipoPostagemEnum.RESPOSTA + "')" \
                  ")" \
                  "ORDER BY relevancia DESC "
            executor.execute(sql, (usuario_id,))
            tuplas_respostas = executor.fetchall()
            self.criador_conexao.fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas_respostas)) + ' resultados')
            return tuplas_respostas
        except Exception as erro:
            self.log.erro('Erro ao buscar respostas do usuario ID: ' + str(usuario_id), erro)
            return str('ERRO: ' + str(erro))

    def buscar_total_respostas(self, id_postagem):
        try:
            self.log.info('Buscando total de respostas da postagem ' + str(id_postagem))
            executor_total_postagem = CriadorConexao.criar_executor()
            sql = "SELECT count(*) " \
                  "FROM postagem " \
                  "WHERE postagem_respondida_id = %s "

            executor_total_postagem.execute(sql, (id_postagem,))
            tupla_total_postagem = executor_total_postagem.fetchone()
            CriadorConexao.fechar_executor()
            self.log.info(str(tupla_total_postagem[0]) + ' respostas para a postagem ' + str(id_postagem))
            return str(tupla_total_postagem[0])
        except Exception as erro:
            self.log.erro('Erro ao buscar o total de respostas da postagem ' + str(id_postagem), erro)
            return str(0)