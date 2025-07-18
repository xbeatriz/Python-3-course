#
# for loops
 
notas = [1,2,3,4,5,6,7,8,9,10]

minha_variavel = 'ola mundo'

notas[0]

#for significa para
for letra in minha_variavel:
    print(letra)

list(range(10))

list(range(5,10))

for numero in range(1,10,2): #em range de 1 a 10, pula de 2 em 2 e o 10 não entra.
    print(numero)

############
##### while loops

# enquanto - while
num = 1
while num <=9:
    print(num)
    #num = num + 2
    num+=2

user = True
while user:
    user_input = input("Quer continiuar? (s/n)")
    if user_input == 'n':
        user = False

