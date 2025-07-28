# Classes
# Escopo local, não-local e global

# O escopo interno, o qual é pesquisado primeiro contém nomes locais
# O escopo de uma função, considerando que o nome já existe de forma local, contém nomes não locais (nonlocal) e mas também não globais
# O escopo externo contém variáveis globais (global)
# O último escopo, pesquisado por último são os nomes built-ins, do próprio python

def teste_escopo():
    def atr_local():
        variavel = 'local'
    def atr_nonlocal():
        nonlocal variavel
        variavel = 'nonlocal'
    def atr_global():
        variavel = 'global'

    atr_local()
    variavel = 'outro'
    print('local', variavel)

    atr_nonlocal()
    print('nonlocal', variavel)

    atr_global()
    print('global', variavel)

teste_escopo()