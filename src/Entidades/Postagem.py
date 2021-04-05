import datetime
import json
from src.Utils import TipoPostagemEnum, SituacaoPostagemEnum


class Postagem:
    id = 0
    data_insercao = ''
    data_alteracao = ''
    titulo = ''
    conteudo = ''
    tipo = ''
    situacao = ''
    postagem_respondida_id = None
    usuario_id = None
    relevancia = 0

    def __init__(self):
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()
        self.postagem_respondida_id = None
        self.relevancia = 0

    def definir_por_json(self, postagem_json):
        if "id" in postagem_json:
            self.id = postagem_json['id']
        self.titulo = postagem_json['titulo']
        self.conteudo = postagem_json['conteudo']
        self.tipo = postagem_json['tipo']
        self.usuario_id = postagem_json['usuarioId']
        self.situacao = SituacaoPostagemEnum.NAO_RESPONDIDA
        if "postagemRespondidaId" in postagem_json:
            self.postagem_respondida_id = postagem_json['postagemRespondidaId']
        if "relevancia" in postagem_json:
            self.relevancia = postagem_json["relevancia"]

    def definir_por_tupla(self, tupla):
        self.id = tupla[0]
        self.data_insercao = tupla[7]
        self.data_alteracao = tupla[1]
        self.titulo = tupla[4]
        self.conteudo = tupla[2]
        self.tipo = tupla[3]
        self.usuario_id = tupla[6]
        self.situacao = tupla[9]
        self.postagem_respondida_id = tupla[5]
        self.relevancia = tupla[8]

    def json(self):
        return json.loads(self.json_string())

    def json_string(self):
        texto_json = '{\n'
        texto_json += '\t\t\"id\": ' + str(self.id) + ',\n'
        texto_json += '\t\t\"titulo\": \"' + self.titulo + '\",\n'
        texto_json += '\t\t\"conteudo\": \"' + self.conteudo + '\",\n'
        texto_json += '\t\t\"tipo\": \"' + self.tipo + '\",\n'
        texto_json += '\t\t\"postagemRespondidaId\": ' \
                      + (str(self.postagem_respondida_id)
                         if self.postagem_respondida_id is not None
                         else 'null') + ',\n'
        texto_json += '\t\t\"usuarioId\": ' + str(self.usuario_id) + ',\n'
        texto_json += '\t\t\"dataInsercao\": \"' + str(self.data_insercao) + '\",\n'
        texto_json += '\t\t\"relevancia\": ' + str(self.relevancia) + ',\n'
        texto_json += '\t\t\"situacao\": \"' + self.situacao + '\"\n'
        texto_json += '}'
        return texto_json

    def __str__(self):
        return self.json_string()
