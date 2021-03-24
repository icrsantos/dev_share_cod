import datetime


def info(texto, classe):
    log_header = '[' + str(datetime.datetime.now()) + ' | ' + str(classe) + ']: '
    print(log_header + texto)


def erro(texto, excecao, classe):
    log_header = '[' + str(datetime.datetime.now()) + ' | ' + str(classe) + ']: '
    print(log_header + texto + ': ' + str(excecao))
