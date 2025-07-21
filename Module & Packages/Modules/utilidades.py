def formata_hora(horas, minutos='00', segundos='00'):
    print(f'{horas}:{minutos}:{segundos}')  # Função que formata horas, minutos e segundos

def soma_simplificada(*args):
    return sum(args)  # Função que soma os argumentos passados

def impar_ou_par(n):
    if n % 2 == 0:
        print(f'{n} é par')  # Verifica se o número é par
    else:
        print(f'{n} é ímpar')
