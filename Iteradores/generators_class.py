# Geradores / generators
# é uma ferramenta simples e poderosa para criar iterators. Eles são escritos como funções comuns, porém usam o yield sempre que eles precisam 
# retornar dados. Cada vez que chama o next(), o gerador pausa aonde parou (e lembra de todos os valores e qual foi o último valor executado).

def inverso(dados):
    for index in range(len(dados)-1, -1, -1): # start | stop | step
        yield dados[index]

for elemento in inverso ('raul'):
    print(elemento)