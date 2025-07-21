4/0 
# ZeroDivisionError: Divisão por zero não é permitida.

2 + tres + 4
# NameError: nome 'tres' não está definido

'3' + 8
# TypeError: não é possível concatenar str e int

num = int(input('Digite um número: ')) # se entrar com uma letra
# ValueError: entrada inválida para conversão de int


# Exemplo de tratamento de erro com try e except
# Aqui, se o user digitar algo que não seja um número, o programa não vai travar, mas vai imprimir uma mensagem de erro.
while True: 
    try: #tente
        num = int(input('Digite um número: '))  # se entrar com uma letra
        print(f'Você digitou o número {num}')  # se for um número, imprime
        break  # sai do loop se for um número
    except ValueError:  # se der erro de valor, executa
        print('Você não digitou um número válido. Tente novamente.')  # mensagem de erro

try:
    pass
except (RuntimeError, TypeError, NameError):
    pass

try:
    pass
except:
    pass

try:
    pass
except RuntimeError:
    pass
except ValueError:
    pass
except:
    pass


while True: 
    try: #tente
        num = int(input('Digite um número: '))  # se entrar com uma letra
        print(f'Você digitou o número {num}')  # se for um número, imprime
        break  # sai do loop se for um número
    except ValueError as erro:  # se der erro de valor, executa
        print('Você não digitou um número válido. Tente novamente.')  # mensagem de erro
        print('Erro:', erro)  # imprime o erro específico

def divisao_por_zero():
    return 2/0

try:
    divisao_por_zero()  # Chamada da função que causa erro
except ZeroDivisionError as erro:
    print('Erro:', erro)

