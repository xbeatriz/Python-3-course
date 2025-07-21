# Função Enumerate 
# A função enumerate() é uma função embutida do Python que permite iterar sobre um objeto iterável (como uma lista, tupla ou string) e obter tanto o índice quanto o valor de cada elemento durante a iteração. Isso é útil quando você precisa acompanhar a posição dos elementos enquanto os percorre.

alfabeto = list('abcdefghijklmnopqrstuvwxyz')  # Lista do alfabeto
print(alfabeto)  # Imprime a lista do alfabeto

idx = 0 # Inicializa o índice
for letra in alfabeto:  # Itera sobre cada letra do alfabeto
    print(f'{idx} - {letra}')  # Imprime o índice e a letra
    idx += 1  # Incrementa o índice

###### com a função enumerate ######
# A função enumerate() simplifica o processo de obter o índice e o valor ao mesmo tempo
for i, letra in enumerate(alfabeto, 0):  # Usa enumerate para obter o índice e a letra
    print(f'{i} - {letra}')  # Imprime o índice e a letra

print(alfabeto.index('a'))  # Imprime o índice da letra 'a'

##### encontrar o índice de um elemento em uma lista ######
# A função enumerate() pode ser usada para encontrar o índice de um elemento em uma lista
def encontra_idx(lista, elemento):
    for idx, el in enumerate(lista):
        if el == elemento:
            return idx
    return print(f'O elemento \'{elemento}\' não foi encontrado na lista.')  # Mensagem se o elemento não for encontrado

encontra_idx(alfabeto, '0')  # Chamada da função para encontrar o índice da letra '0'

