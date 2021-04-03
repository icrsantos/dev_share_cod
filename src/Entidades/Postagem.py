import datetime
from flask import jsonify
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
    postagem_respondida_id = ''
    usuario_id = 0

    def __init__(self):
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()

    def definir_por_json(self, postagem_json):
        self.id = postagem_json['id']
        self.titulo = postagem_json['titulo']
        self.conteudo = postagem_json['conteudo']
        self.tipo = postagem_json['tipo']
        self.usuario_id = postagem_json['usuarioId']
        self.situacao = SituacaoPostagemEnum.NAO_RESPONDIDA
        self.postagem_respondida_id = postagem_json['postagemRespondidaId']


class PostagemDTO:
    def __init__(self, tuplas):
        lista_postagem = ''
        if len(tuplas) > 1:
            lista_postagem += '[\n'
        for tupla in tuplas:
            lista_postagem += '\t{\n'
            lista_postagem += '\t\t\"id\": ' + str(tupla[0]) + ',\n'
            lista_postagem += '\t\t\"titulo\": \"' + tupla[4] + '\",\n'
            lista_postagem += '\t\t\"conteudo\": \"' + tupla[2] + '\",\n'
            lista_postagem += '\t\t\"tipo\": \"' + tupla[3] + '\",\n'
            lista_postagem += '\t\t\"postagemRespondidaId\": ' \
                              + (str(tupla[5]) if tupla[5] is not None else 'null') + ',\n'
            lista_postagem += '\t\t\"usuarioId\": ' + str(tupla[6]) + ',\n'
            lista_postagem += '\t\t\"dataInsercao\": \"' + str(tupla[7]) + '\",\n'
            lista_postagem += '\t\t\"relevancia\": ' + str(tupla[8]) + ',\n'
            lista_postagem += '\t\t\"situacao\": \"' + tupla[9] + '\"\n'
            if tuplas.index(tupla) != (len(tuplas) - 1):
                lista_postagem += '\t},\n'
            else:
                lista_postagem += '\t}\n'
        if len(tuplas) > 1:
            lista_postagem += ']'
        self.texto_json = lista_postagem

    def __str__(self):
        return self.texto_json

    def json(self):
        return json.loads(self.texto_json)
