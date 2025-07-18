# Métodos e funções em Classes

# Função 	Um bloco de código que pode ser chamado por nome, 
# definido com def. Pode ou não receber argumentos e pode retornar algo. 
# Ex.: print(), len(), min(), ou uma função que tu crias.

# Método Uma função associada a um objeto (geralmente um tipo como string, lista, dicionário, etc). 
# É chamada com objeto.metodo().


# Métodos ligados as classes de objetos
print(int('3')) # converte a string '3' para inteiro
print(float('3.14')) # converte a string '3.14' para float
print(float(3))  # converte o inteiro 3 para float
print('Ola') # converte a string 'Ola' para string (não muda nada)
print(str(10.4)) # converte o float 10.4 para string
print(len('ola')) # retorna o comprimento da string 'ola'
print(len([1, 2, 3])) # retorna o comprimento da lista [1, 2, 3]
print(len({3,4,5,3})) # retorna o comprimento do conjunto {3, 4, 5, 3} # (duplicados são ignorados em conjuntos)
sum((3,5,6)) # soma os elementos do iterável (tupla neste caso) e retorna 14
min ([1,2,3]) # retorna o menor valor da lista [1, 2, 3]
max ([1,2,3]) # retorna o maior valor da lista [1,  2, 3]
round(13.4938737373)
round(13.5938737373)
round(13.5938737373, 2) # arredonda o número para duas casas decimais


# Funções
def minha_funcao_imprimir():
    print("Olá, esta é a minha função!")

def soma_dois_numeros(valor1, valor2):
    """
    Esta função recebe dois números e retorna a soma deles.
    exemplo de uso:
    resultado = soma_dois_numeros(5, 10)
    :param valor1: Primeiro número a ser somado.
    :param valor2: Segundo número a ser somado.
    :return: A soma dos dois números.
    """
    return valor1 + valor2

print(soma_dois_numeros(8,8))  # Chama a função e imprime o resultado
