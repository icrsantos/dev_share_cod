from src.BancoDeDados import CriadorConexao


class PostagemRepositorio:
    def __init__(self):  # Construtora:
        self.conexao = None

    def buscar_postagens(self, texto_pesquisa):
        try:
            self.conexao = CriadorConexao.criar_conexao()
            mycursor = self.conexao.cursor()
            sql = "SELECT * FROM postagem WHERE (" \
                  "(titulo like '%%%s%%') OR" \
                  "(conteudo like '%%%s%%') OR" \
                  "(tipo_postagem like '%%%s%%')" \
                  ")" \
                  "ORDER BY relevacia DESC "
            parametros = texto_pesquisa
            mycursor.execute(sql, parametros)
            resultados = mycursor.fetchall()
            self.conexao.close()
            return str(resultados)
        except Exception as erro:
            print('Erro ao buscar postagens: ' + str(erro))
            return []
