# comparar bytecodes

from dis import dis

print(dis('{1}')) # esta forma é melhor
print(dis('set([1])'))

# compreensão de sets
abc = list('andabkdbajkdsa')

ord('a') # este vai dar o valor do a em unicode, existe um valor para cada caracter

print({ord(letra) for letra in abc}) # não vamos ter a repetição de valor nenhum 

print({str(ord(letra)) for letra in abc}) # transforma em string

# sintaxe quando tem apenas o if
print({str(ord(letra)) for letra in abc if ord(letra) <= 105}) # condicional: retornar apenas valores menores ou iguais a 105

# sintaxe if e else
print({str(ord(letra)) if ord(letra) <= 105 else ord(letra) for letra in abc}) # se for if else, vai ser invertido