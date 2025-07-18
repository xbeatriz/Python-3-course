#if, else e elif
# Condicionais em Python

#if - se
#else - senão
#elif - senão se

devo_continuar = True


if devo_continuar == True:
    print("Continuando o processo...")
# Não é necessário comparar com True, pode-se simplificar que faz o mesmo que o anterior:
if devo_continuar:
    print("Continuando o processo...")

pessoas_conhecidas = ['João', 'Maria', 'José', 'Ana']
pessoa = input("Digite o nome de uma pessoa: ")
pessoa
if pessoa in pessoas_conhecidas:
    print("Pessoa conhecida.")
else:
    print("Pessoa desconhecida.")  

if pessoa not in pessoas_conhecidas:
    print("Pessoa desconhecida.")

#Função da temperatura
# Desenvolva um programa que recebe a temperatura e informa se a pessoa está com febre ou não:
# - Menor que 36º - Hipotermia
# - Entre 36º e 37,5º - Normal
# - Acima de 37,5º até 39,5º - Febre
# - Acima de 39,5º até 41º - Febre alta
# - Acima de 41º - Hipertermia

temperatura = float(input('Por favor colocar a temperatura corportal:'))

if temperatura < 36:
    print('Hipotermia')
elif temperatura >= 36 and temperatura < 37.5:
    print('Temperatura normal')
elif temperatura >= 37.5 and temperatura < 39.5:
    print('Febre')
elif temperatura >= 39.5 and temperatura < 41:
    print('Febre alta')
elif temperatura >= 41:
    print('Hipertemia')

#Função da temperatura
temperatura = float(input('Por favor colocar a temperatura corportal:'))

if temperatura < 36:
    print('Hipotermia')
elif (temperatura >= 36) & (temperatura < 37.5):
    print('Normal')
elif (temperatura >= 37.5) & (temperatura < 39.5):
    print('Febre')
elif (temperatura >= 39.5) & (temperatura < 41):
    print('Febre alta')
else:
    print('Hipertemia')


# Exercicio 2
# Desenvolva um programa que recebe a idade e informa se a pessoa pode votar ou não. 
# - Quem tem menos de 16 anos não pode votar
# - Quem tem 16 ou 17 é opcional
# - Entre 18 e 69 é obrigatório
# - Dos 70 anos para cima é opcional

idade = int(input('Por favor, informe a sua idade: '))

if idade < 16: 
    print('Não pode votar')
elif idade >= 16 and idade < 18:
    print('Voto opcional')
elif idade >= 18 and idade < 70:
    print('Voto obrigatório')
else:
    print('Voto opcional')


if idade < 16: 
    print('Não pode votar')
elif (idade == 16) | (idade ==17) | (idade == 70):
    print('Voto opcional')
else:
    print('Voto obrigatório')