import functools

def meu_decorador(func):
    @functools.wraps(func)
    def funcao_que_roda_func():
        print("***************EMBRULHADO FUNCAO*************")
        func()
        print("***************FECHANDO FUNCAO*************")
    return funcao_que_roda_func

@meu_decorador
def minha_funcao():
    print('Sou uma funcao')

minha_funcao()