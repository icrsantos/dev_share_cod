import datetime


class Postagem:
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
