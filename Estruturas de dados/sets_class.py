#SETS é uma coleção não ordenada, imutável em termos de estrtura (mas mutável em conteúdo)
# e não permite elementos duplicados

set_notas = {3,4,3,5,5,9,7,8}
# sets não suportam indexamento
#set_notas[0] # TypeError: 'set' object is not subscriptable

print(set_notas)
# Adicionando um novo elemento
set_notas.add(10)
print(set_notas)
