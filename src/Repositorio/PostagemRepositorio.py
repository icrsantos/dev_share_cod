from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger
from src.Utils import TipoPostagemEnum


class PostagemRepositorio:
    def __init__(self):  # Construtora:
        self.conexao = None
        self.log = Logger('PostagemRepositorio')

    def criar_executor(self):
        self.conexao = CriadorConexao.criar_conexao()
        return self.conexao.cursor()

    def commit_mudancas(self):
        self.conexao.commit()

    def fechar_executor(self):
        self.conexao.close()

    def buscar_postagens(self, texto_pesquisa):
        try:
            self.log.info('Buscando posts com a mensagem \'' + texto_pesquisa + '\'')
            executor = self.criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(titulo like '%" + texto_pesquisa + "%') OR " \
                  "(conteudo like '%" + texto_pesquisa + "%') OR " \
                  "(tipo like '%" + texto_pesquisa + "%')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            executor.execute(sql)
            tuplas = executor.fetchall()
            self.fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar postagem', erro)
            return str('ERRO: ' + str(erro))

    def criar(self, postagem):
        try:
            self.log.info('Inserindo nova postagem')
            executor = self.criar_executor()
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
            self.commit_mudancas()
            self.fechar_executor()
            id_criacao = str(executor.lastrowid)
            self.log.info('Criada a postagem ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir postagem', erro)
            return str(0)

    def buscar_respostas_a_postagem(self, postagem_id):
        try:
            self.log.info('Buscando respostas ao post ID: ' + str(postagem_id))
            executor = self.criar_executor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(postagem_respondida_id = " + str(postagem_id) + " ) AND " \
                  "(tipo = '" + TipoPostagemEnum.RESPOSTA + "')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            executor.execute(sql)
            tuplas = executor.fetchall()
            self.fechar_executor()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar respostas da postagem ID: ' + str(postagem_id), erro)
            return str('ERRO: ' + str(erro))
