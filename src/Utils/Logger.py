import datetime


class Logger:
    nome_classe = ''

    def __init__(self, nome_classe):
        self.nome_classe = nome_classe

    def info(self, texto):
        log_header = '[' + str(datetime.datetime.now()) + ' | ' + self.nome_classe + ']: '
        print(log_header + texto)

    def erro(self, texto, excecao):
        log_header = '[' + str(datetime.datetime.now()) + ' | ' + self.nome_classe + ']: '
        print(log_header + texto + ': ' + str(excecao))
