import datetime
import json


class Notificacao:
    def __init__(self):
        self.id = 0
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()
        self.tipo = ''
        self.postagem_id = ''
        self.usuario_notificado_id = ''
        self.mensagem_enviada = ''
        self.nova_notificacao = ''

    def definir_por_tupla(self, tupla):
        self.id = tupla[0]
        self.data_insercao = tupla[1]
        self.data_alteracao = tupla[2]
        self.tipo = tupla[3]
        self.postagem_id = tupla[4]
        self.usuario_notificado_id = tupla[5]
        self.mensagem_enviada = tupla[6]
        self.nova_notificacao = tupla[7]

    def definir_por_json(self, notificacao_json):
        self.id = notificacao_json['id']
        self.postagem_id = notificacao_json['postagem_id']
        self.usuario_notificado_id = notificacao_json['usuario_notificado_id']
        self.tipo = notificacao_json['tipo']
        self.mensagem_enviada = notificacao_json['mensagem_enviada']
        self.data_insercao = notificacao_json['data_insercao']
        self.nova_notificacao = notificacao_json["nova_notificacao"]
        self.data_alteracao = notificacao_json["data_alteracao"]

    def json_string(self):
        texto_json = '{\n'
        texto_json += '\t\t\"id\": ' + str(self.id) + ',\n'
        texto_json += '\t\t\"postagem_id\": ' + str(self.postagem_id) + ',\n'
        texto_json += '\t\t\"usuario_notificado_id\": ' + str(self.usuario_notificado_id) + ',\n'
        texto_json += '\t\t\"tipo\": \"' + self.tipo + '\",\n'
        texto_json += '\t\t\"mensagem_enviada\": \"' + str(self.mensagem_enviada) + '\",\n'
        texto_json += '\t\t\"data_insercao\": \"' + str(self.data_insercao) + '\",\n'
        texto_json += '\t\t\"nova_notificacao\": \"' + str(self.nova_notificacao) + '\",\n'
        texto_json += '\t\t\"data_alteracao\": \"' + str(self.data_alteracao) + '\"\n'
        texto_json += '}'
        return texto_json

    def __str__(self):
        return self.json_string()

    def json(self):
        return json.loads(self.json_string())