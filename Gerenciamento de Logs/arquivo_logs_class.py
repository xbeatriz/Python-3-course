# Levels of logs
# debug - informação detalhada, tipicamente de interesse quando diagnosticando problemas.
# info - confirmação que as coisas estão funcionando conforme o esperado
# warning - uma indicação que uma coisa inesperada aconteceu, ou inidicativo de um problemas no futuro proximo
# error - devido a problemas mais sérios, o software não foi capaz de performar alguma tarefa
# critical - um problema sério, indicando que o próprio programa esteja incapaz de continuar rodando

#https://docs.python.org/3/library/logging.html

import logging

logging.basicConfig(filename='animal.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class Animal: 
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        logging.warning(f'Animal de nome "{self.nome} e tipo "{self.tipo}" criado!')

cao = Animal('Rufus', 'canino')
gato = Animal('Mia', 'felino')