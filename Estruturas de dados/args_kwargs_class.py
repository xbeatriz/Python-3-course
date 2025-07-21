################## ARGUMENTOS ######################
def soma_dois_numeros(arg1, arg2):
    return arg1 + arg2  # Função que soma dois números
print(soma_dois_numeros(5, 10))  # Chamada da função para somar dois números

def soma_cinco_numeros(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5  # Função que soma cinco números
print(soma_cinco_numeros(1, 2, 3, 4, 5))  # Chamada da função para somar cinco números
# Neste caso, se eu nao passar os cinco argumentos, a função vai dar erro. 


# E se eu não souber a quantidade de argumentos que vou passar?
def minha_lista_somada(lista_arg):
    return sum(lista_arg)  # Função que soma os elementos de uma lista
print(minha_lista_somada([1, 2, 3, 4, 5]))  # Chamada da função para somar uma lista de números

# Porém, também posso utilizar *args para passar uma quantidade de argumentos que não sei quantos são 
def soma(*args):
    return sum(args)  # Função que soma os argumentos passados
print(soma(1, 2, 3, 4, 5))  # Chamada da função para somar vários números

# desempacotar args de listas
list(range(1, 10, 2))
argumentos = [1, 10, 2] # a palavra pode ser qualquer coisa, o que identifica é o * antes do nome da minha variável
print(list(range(*argumentos)))  # Chamada da função range com desempacotamento de args

args_tupla =(1, 10, 2)  # Tupla de argumentos
print(list(range(*args_tupla)))  # Chamada da função range com desempacotamento de args de uma tupla



########## KWARGS ##########
# kwargs é uma abreviação de "keyword arguments" e permite passar argumentos nomeados para uma função.

# args ==> argumentos
# kwargs ==> keyword arguments (argumentos de palavras-chave)

def args_kwargs(*args, **kwargs): # aqui pode ser qualquer palavra, mas é comum usar args e kwargs
    print(args)  # Imprime os argumentos posicionais
    print(kwargs)  # Imprime os argumentos nomeados

# os kwargs são passados como um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores correspondentes.
# os kwargs vêm só depois dos args, ou seja, primeiro você passa os argumentos posicionais e depois os nomeados.
(args_kwargs(1, 2, 3, nome='Joao', idade=30))  # Chamada da função com args e kwargs
# aqui os args são os números 1, 2 e 3, e os kwargs são nome='Joao' e idade=30

# Desempacotando kwargs de dicionários
# aqui eu sou obrigada a passar as horas, os minutos e os segundos não preciso de passar, pois eles têm valores padrão
# se não passar as horas, a função vai dar erro
def formata_horas(horas, minutos = '00', segundos = '00'):
    print(f'{horas}:{minutos}:{segundos}')  # Função que formata horas, minutos e segundos

tempo = {
    'horas': 10,
    'minutos': 30,
    'segundos': 45
}

formata_horas(**tempo)  # Chamada da função com desempacotamento de kwargs de um dicionário
formata_horas('12')
formata_horas(horas='13')
formata_horas(**{'horas': '10'})

