from src.BancoDeDados import CriadorConexao
from src.Utils.Logger import Logger


class PostagemRepositorio:
    def __init__(self):  # Construtora:
        self.conexao = None
        self.log = Logger('PostagemRepositorio')

    def buscar_postagens(self, texto_pesquisa):
        try:
            self.log.info('Buscando posts com a mensagem \'' + texto_pesquisa + '\'')
            self.conexao = CriadorConexao.criar_conexao()
            mycursor = self.conexao.cursor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(titulo like '%" + texto_pesquisa + "%') OR " \
                  "(conteudo like '%" + texto_pesquisa + "%') OR " \
                  "(tipo like '%" + texto_pesquisa + "%')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            mycursor.execute(sql)
            tuplas = mycursor.fetchall()
            self.conexao.close()
            self.log.info('Encontrados ' + str(len(tuplas)) + ' resultados')
            return tuplas
        except Exception as erro:
            self.log.erro('Erro ao buscar postagem', erro)
            return str('ERRO: ' + str(erro))

    def criar(self, postagem):
        try:
            self.log.info('Inserindo nova postagem')
            self.conexao = CriadorConexao.criar_conexao()
            mycursor = self.conexao.cursor()
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
            mycursor.execute(sql, parametros)
            self.conexao.commit()
            self.conexao.close()
            id_criacao = str(mycursor.lastrowid)
            self.log.info('Criada a postagem ID: ' + id_criacao)
            return id_criacao
        except Exception as erro:
            self.log.erro('Erro ao inserir postagem', erro)
            return str(0)
