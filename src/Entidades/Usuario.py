import datetime


class Usuario:
    data_insercao = ''
    data_alteracao = ''
    nome = ''
    senha = ''
    email = ''

    def __init__(self, _nome, _email, _senha):  # Construtora:
        self.data_insercao = datetime.datetime.now()
        self.data_alteracao = datetime.datetime.now()
        self.nome = _nome
        self.email = _email
        self.senha = _senha
