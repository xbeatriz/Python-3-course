####### finally ##########
# O bloco finally é sempre executado, independentemente de um erro ter ocorrido ou não.
try:
    raise TypeError
finally:
    print('Isso sempre será executado, independentemente de um erro ter ocorrido ou não')

####### else ##########
# O bloco else é executado se não ocorrer nenhum erro no bloco try.
try: 
    raise NameError
except NameError:
    print('Ocorreu um erro de nome')
else:
    print('Não ocorreu nenhum erro')

####### else e finally ##########
# O bloco else é executado se não ocorrer nenhum erro no bloco try, e o bloco finally é sempre executado.
def divide(x,y):
    try: 
        resultado = x / y  # Tenta dividir x por y
    except ZeroDivisionError as zero:  # Captura o erro de divisão por zero
        print('Erro:', zero)
    else:
        print('Resultado da divisão:', resultado)
    finally:
        print('Fim da execução da função divide')

divide(10, 2)  # Chamada da função divide com argumentos válidos

