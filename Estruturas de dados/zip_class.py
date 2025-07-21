# Função zip()
# A função zip() é usada para combinar elementos de duas ou mais listas (ou iteráveis) em tuplas.

l1 = 'banana batata couve frango'.split()  # Lista de strings
print(l1)  # Imprime a lista de strings

l2 = ' fruta legumes verdura carne'.split()  # Outra lista de strings
print(l2)  # Imprime a segunda lista de strings

lista_zipada = zip(l1, l2)  # Combina as duas listas em tuplas
print(lista_zipada)  # Imprime o objeto zip, que é um iterador
print(list(lista_zipada))  # Converte o objeto zip em uma lista de tuplas

indexes = range(4) # Cria um range de índices de 0 a 3
campos = 'nome idade sexo cidade'.split()  # Lista de campos
dados = 'beatriz 25 feminino porto'.split()  # Lista de dados
list(zip(indexes, campos, dados))  # Combina os índices, campos e dados em tuplas
print(list(zip(indexes, campos, dados)))  # Imprime a lista de tuplas combinadas

for idx, campo, dado in zip(indexes, campos, dados):  # Itera sobre os índices, campos e dados
    print(f'{idx}| ({campo}): {dado}')  # Imprime o campo, índice e dado formatados