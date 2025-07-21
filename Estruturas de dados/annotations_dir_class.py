def soma(a: int, b: int):
    """soma a+b"""
    return a + b  # Função que soma dois números

print(soma.__doc__)

print(dir(soma))  # Mostra os atributos e métodos da função soma

print(soma.__annotations__)  # Mostra as anotações da função soma

def f(a: str = '', b: int = 0, c: float = 0.0, d: bool = None):
    """minha função mista
    aqui é a documentação da função f"""
    print(f.__annotations__)  # Mostra as anotações da função f
f('a', 1, 4.3, False)  # Chamada da função f com argumentos
print(f.__doc__)  # Mostra a documentação da função f
f()
print(f.__annotations__)  # Mostra as anotações da função f após a chamada


####### math

import math  # Importa o módulo math
print(dir(math))  # Mostra os atributos e métodos do módulo math

print(math.sqrt(9)) # Mostra a raiz quadrada de 9
print(math.pi)  # Mostra o valor de pi
print(math.sin(180)) # Mostra o seno de 180 graus
print(math.pow(2, 3))  # Mostra 2 elevado a 3
print(math.pow.__doc__)  # Mostra a documentação do método pow do módulo math


