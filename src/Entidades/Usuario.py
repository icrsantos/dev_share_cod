import datetime
import json


class Usuario:
    def __init__(self):  # Construtora:
        self.id = None
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()
        self.nome = ''
        self.senha = ''
        self.email = ''
        self.pontos = 0
        self.provedor = ''

    def definir_por_json(self, usuario_json):
        if "id" in usuario_json:
            self.id = usuario_json["id"]
        if "dataInsercao" in usuario_json:
            self.data_insercao = usuario_json["dataInsercao"]
        if "dataAlteracao" in usuario_json:
            self.data_alteracao = usuario_json["dataAlteracao"]
        if "pontos" in usuario_json:
            self.pontos = usuario_json["pontos"]
        if "provedor" in usuario_json:
            self.pontos = usuario_json["provedor"]
        self.nome = usuario_json["nome"]
        self.email = usuario_json["email"]
        self.senha = usuario_json["senha"]

    def definir_por_tupla(self, tupla):
        self.id = tupla[0]
        self.data_insercao = tupla[5]
        self.data_alteracao = tupla[1]
        self.nome = tupla[3]
        self.email = tupla[2]
        self.senha = tupla[4]
        self.pontos = tupla[6]
        self.provedor = tupla[7]

    def json(self):
        return json.loads(self.__str__())

    def __str__(self):
        texto_json = '{\n'
        texto_json += '\t\"id\": ' + str(self.id) + ',\n'
        texto_json += '\t\"dataAlteracao\": \"' + str(self.data_alteracao) + '\",\n'
        texto_json += '\t\"email\": \"' + self.email + '\",\n'
        texto_json += '\t\"nome\": \"' + self.nome + '\",\n'
        texto_json += '\t\"senha\": \"' + self.senha + '\",\n'
        texto_json += '\t\"provedor\": \"' + self.provedor + '\",\n'
        texto_json += '\t\"pontos\": \"' + str(self.pontos) + '\",\n'
        texto_json += '\t\"dataInsercao\": \"' + str(self.data_insercao) + '\"\n'
        texto_json += '}\n'
        return texto_json
