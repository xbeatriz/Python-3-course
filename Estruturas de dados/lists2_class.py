# como representar uma lista
# exemplo 1
minha_lista = [1, 2, 3, 4, 5]
# exemplo 2
[x for x in range(5)] # ele vai adicionar para cada x dentro do range(5) o valor de x

[x**2 for x in range(5)] # ele vai adicionar o quadrado de cada x dentro do range(5)

[x for x in range(10) if x % 2 == 0] # ele vai adicionar apenas os números pares dentro do range(10)

pessoas_conhecidas = [' Beatriz', 'João', ' maria', 'PEDRO']

' Beatriz'.strip() # ele vai remover os espaços em branco no início e no final da string
'João'.lower() # ele vai deixar a string em letras minúsculas
'maria'.upper() # ele vai deixar a string em letras maiúsculas
'PEDRO'.capitalize() # ele vai deixar a primeira letra da string em maiúscula e o restante em minúsculas

pessoas_conhecidas[2].strip().capitalize() # ele vai remover os espaços em branco no início e no final da string, deixar a primeira letra em maiúscula e o restante em minúsculas

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas_conhecidas]
pessoas_normalizadas

# listas com mais de um for
amigos_de_fred = ['josi', 'felipe', 'maria']
amigos_de_davi = ['joão', 'pedro', 'maria']

# af ==> amigo de fred
# ad ==> amigo de davi
[af for af in amigos_de_fred for ad in amigos_de_davi if af == ad]

amigos_em_comum = [af for af in amigos_de_fred if af in amigos_de_davi]
amigos_em_comum

[(af, ad) for af in amigos_de_fred for ad in amigos_de_davi if af != ad]

for af in amigos_de_fred:
    for ad in amigos_de_davi:
        if af != ad:
            print(af,ad)