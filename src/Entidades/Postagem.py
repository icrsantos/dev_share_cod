import datetime


class Postagem:
    data_insercao = ''
    data_alteracao = ''
    titulo = ''
    conteudo = ''
    tipo = ''
    postagem_respondida_id = ''
    usuario_id = ''

    def __init__(self):
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()
