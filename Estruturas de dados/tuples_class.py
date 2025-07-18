# tipo de estrutura de dados para armazenar uma coleção ordenada e imutável de elementos
# ordenadas, imutáveis, podem conter tipos diferentes de dados, permitem elementos duplicados.

notas_tuplas = (3, 4, 5, 1)
print(notas_tuplas)

print(notas_tuplas[0])
notas_tuplas = notas_tuplas + (7,) # tenho de colocar a virgula se adicionar apenas um numero se for mais do que um nao preciso (5,7)
print(notas_tuplas)
notas_tuplas += (8,)
print(notas_tuplas)