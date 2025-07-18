# a melhor forma
notas = [1, 10, 5, 7, 8, 8]

len(notas) #quantidade de elementos em notas
sum(notas) # soma os valores
media = sum(notas)/len(notas)
media
notas.append(10) # adiciona o 10 ao array
notas.pop() # vai retirar o último elemento adicionado

# Indexar e slicing listas
notas[0] # primeiro elemento 
notas[:3] # vai buscar o index 0, 1 e 2

# listas/arrays são mutáveis
notas[2] = 777

# fibonacci
# 0 1 1 2 3 5 8 13 21 ... 
# é a soma dos dois valores anteriores ao que eu estou a escrever
fibo = [0,1]
fibo.append(fibo[-2] + fibo[-1])
fibo

# forma diferente de executar o mesmo de cima só que com uma variável
prox_elemento = fibo[-2] + fibo[-1]
fibo.append(prox_elemento)
fibo
