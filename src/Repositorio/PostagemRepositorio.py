from src.BancoDeDados import CriadorConexao
from src.Utils import Logger
from src.Entidades.Postagem import ListaPostagensDTO


class PostagemRepositorio:
    def __init__(self):  # Construtora:
        self.nome_classe = 'PostagemRepositorio'
        self.conexao = None

    def buscar_postagens(self, texto_pesquisa):
        try:
            Logger.info('Buscando postagens com a mensagem \'' + texto_pesquisa + '\'', self.nome_classe)
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
            Logger.info('Encontrados ' + str(len(tuplas)) + ' resultados', self.nome_classe)
            return tuplas
        except Exception as erro:
            Logger.erro('Erro ao buscar postagem', erro, self.nome_classe)
            return str('ERRO: ' + str(erro))

    def criar(self, postagem):
        try:
            Logger.info('Inserindo nova postagem', self.nome_classe)
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
            Logger.info('Criada a postagem ID: ' + id_criacao, self.nome_classe)
            return id_criacao
        except Exception as erro:
            Logger.erro('Erro ao inserir postagem', erro, self.nome_classe)
            return str(0)
