with open('Leitura e Escrita de arquivos/udemy.txt', 'w') as f: # w ==> escrever
    pass

with open('Leitura e Escrita de arquivos/udemy.txt', 'w') as f: # w ==> escrever
    f.write('Uma frase qualquer\n')
    f.write('Uma segunda frase\n')

# sempre que eu faço um novo 'w' o ficheiro é reescrito. Ou seja, neste caso, as frases anteriores saem e fica esta única frase. 
with open('Leitura e Escrita de arquivos/udemy.txt', 'w') as f: # w ==> escrever
    f.write('Terceira frase\n')

# se eu quiser escrever algo que seja para adicionar ao ficheiro, então o W ==> a
with open('Leitura e Escrita de arquivos/udemy.txt', 'a') as f: # a ==> append ==> Adicionar
    f.write('Segunda frase frase frase\n')

texto = """
Ser dev é passar metade do tempo tentando entender código que você 
escreveu semana passada, 
e a outra metade explicando para o cliente que 
só mudar uma coisinha' pode quebrar tudo.
"""

with open('Leitura e Escrita de arquivos/udemy.txt', 'w') as f: 
    f.write(texto)