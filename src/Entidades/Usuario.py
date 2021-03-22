class Usuario:
    nome = ''
    senha = ''
    email = ''

    def __init__(self, _nome, _email, _senha):  # Construtora:
        self.nome = _nome
        self.email = _email
        self.senha = _senha
