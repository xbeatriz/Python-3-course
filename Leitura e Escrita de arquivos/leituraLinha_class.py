# ler um arquivo

#  da forma não recomendada
f = open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') # r ==> read (ler)
texto = f.read()
print(f.closed) # False
f.close()
print(f.closed) # True
print(texto)

# da forma recomendada
with open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') as f: # r ==> read (ler)
    texto = f.read()
    print(texto)
    print(f.closed) # false
print(f.closed) # true

# ler apenas uma linha
with open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') as f: # r ==> read (ler)
    texto = f.readline()
    print(texto, end='')
    
    texto = f.readline()
    print(texto, end='')

with open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') as f: # r ==> read (ler), o f é o nome do ficheiro, pode ser qualquer coisa
    for linha in f:
        print(linha, end='')