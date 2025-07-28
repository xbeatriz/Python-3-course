with open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') as f: # r ==> read (ler)
    texto = f.read(84) # numero de caracteres que vai ler
    print(texto, end='')

    texto = f.read(84) # numero de caracteres que vai ler
    print(texto, end='')

    texto = f.read(84) # numero de caracteres que vai ler
    print(texto, end='')


with open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') as f: # r ==> read (ler)
    qtd = 10 # quantidade de caracteres
    texto = f.read(qtd)
    while len(texto) > 0:
        print(texto, end='')
        texto = f.read(qtd)