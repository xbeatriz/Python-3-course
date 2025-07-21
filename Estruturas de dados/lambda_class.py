# Lambda expressions são funções anónimas, ou seja funções sem nome,
# que são escritas de forma compacta em uma única linha.
# Podem ser usadas para criar funções simples de forma rápida e eficiente.
# Geralmente como argumento de outra função (como map, filter, sorted, etc)

ola = lambda : print('Hello World')  # Função lambda que imprime 'Hello World'
ola()  # Chamada da função lambda

def eleva_ao_quadrado(x):
    return x ** 2  # Função que eleva um número ao quadrado

print(eleva_ao_quadrado(2)) 

aoquadrado = lambda x: x ** 2  # Função lambda que eleva um número ao quadrado
print(aoquadrado(3))



def soma_dois_numeros(a,b): 
    return a + b  # Função que soma dois números

print(soma_dois_numeros(2, 3))

soma = lambda a, b: a + b  # Função lambda que soma dois números
print(soma(2, 3))  # Chamada da função lambda

def impar_ou_par(n):
    if n % 2 == 0:
        print(f'{n} e par')
    else:
        print(f'{n} e ímpar')
print(impar_ou_par(4))  # Chamada da função para verificar se 4 é par ou ímpar


impar_par = lambda n:print(f'{n} e par') if n % 2 == 0 else print(f'{n} e ímpar')  # Função lambda para verificar par ou ímpar 
# aqui o if tem que ser escrito colocado depois do resultado que queremos retornar
print(impar_par(344))  # Chamada da função lambda para verificar se 5 é par ou ímpar 