import datetime
import json


class Curtida:
    def __init__(self):
        self.id = 0
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()
        self.usuario_id = ''
        self.postagem_id = ''
        self.operacao = ''

    def definir_por_tupla(self, tupla_notificacao):
        self.id = tupla_notificacao[0]
        self.data_insercao = tupla_notificacao[1]
        self.data_alteracao = tupla_notificacao[2]
        self.usuario_id = tupla_notificacao[3]
        self.postagem_id = tupla_notificacao[4]
        self.operacao = tupla_notificacao[5]

    def definir_por_json(self, curtida_json):
        self.id = curtida_json['id']
        self.data_insercao = curtida_json['data_insercao']
        self.data_alteracao = curtida_json["data_alteracao"]
        self.postagem_id = curtida_json['postagem_id']
        self.usuario_id = curtida_json['usuario_id']
        self.operacao = curtida_json['operacao']

    def json_string(self):
        texto_json = '{\n'
        texto_json += '\t\t\"id\": ' + str(self.id) + ',\n'
        texto_json += '\t\t\"data_insercao\": \"' + str(self.data_insercao) + '\",\n'
        texto_json += '\t\t\"data_alteracao\": \"' + str(self.data_alteracao) + '\",\n'
        texto_json += '\t\t\"postagem_id\": ' + str(self.postagem_id) + ',\n'
        texto_json += '\t\t\"usuario_id\": ' + str(self.usuario_id) + ',\n'
        texto_json += '\t\t\"operacao\": ' + str(self.operacao) + '\n'
        texto_json += '}'
        return texto_json

    def __str__(self):
        return self.json_string()

    def json(self):
        return json.loads(self.json_string())