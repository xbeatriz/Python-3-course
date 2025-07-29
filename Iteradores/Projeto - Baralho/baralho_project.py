import collections

Carta = collections.namedtuple('Carta', ['valor', 'naipe'])

# 2,10 + 'J', 'Q', 'K', 'A'
# [str(n) for n in range(2,11)]
# list('JQKA')

valores = [str(n) for n in range(2,11)] + list('JQKA')
print(valores)

naipes = 'espadas ouros paus copas'.split()
print(naipes)

cartas = [Carta(valor, naipe) for naipe in naipes for valor in valores] # criar o baralho de cartas
print(cartas)
print(len(cartas)) # número de cartas = 52


# como classe
class Baralho:
    valores = [str(n) for n in range(2,11)] + list('JQKA')
    naipes = 'espadas ouros paus copas'.split()

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in naipes for valor in valores] # criar o baralho de cartas

    def __len__(self):
        return len(self.cartas)
    
    def __getitem__(self, posicao):
        return self.cartas[posicao]

baralho = Baralho()
print(len(baralho))
print(baralho[0]) # primeiro
print(baralho[-1]) # último

# Cartas aleatórias
from random import choice

print(choice(baralho))

# slicing
baralho[11::13]
baralho[::-1]

# iterar e descobrir carta no baralho
print(Carta('K', 'copas') in baralho)