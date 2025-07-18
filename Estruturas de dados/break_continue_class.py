for num in range(10):
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        #print('{} é impar'.format(num))
        #print(num, 'é impar')
        print(str(num) + ' é impar')

for num in range(10):
    if num % 2 == 0: # resto da divisão por 2 é igual a 0
        print(f'{num} é par')
        continue #passa para o próximo
    else:
        print(f'{num} é impar')


for num in range(10):
    if num % 2 == 0: # resto da divisão por 2 é igual a 0
        print(f'{num} é par')
        break #interrompe o loop assim que encontra o primeiro número par
    else:
        print(f'{num} é impar')


for numero in range(2,10):
    for divisor in range(2, numero):
        if numero % divisor == 0:
            print(f'{numero} é divisivel por {divisor}')
            break
        else:
            print(numero, ' é primo')