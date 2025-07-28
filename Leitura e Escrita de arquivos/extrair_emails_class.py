# extrair emails

texto = """
Tetxo antes
ga_to@gmail.com
pa-to@ahoo.com
No meio alguns textos
pata1995@meu-email.edu
rato2020@hotmail.com
k@email.net
E depois alguns textos
"""

with open('Leitura e Escrita de arquivos/emails.txt', 'w') as f: 
    f.write(texto)

with open('Leitura e Escrita de arquivos/emails.txt', 'r') as f:
    for n_linha, linha in enumerate(f):
        print(n_linha,linha, end='')

import re

f = open('Leitura e Escrita de arquivos/so_emails.txt', 'w')
p = re.compile(r'[\w-]+@[\w-]+\.\w+')
with open ('Leitura e Escrita de arquivos/emails.txt') as emails:
    for linha in emails:
        for match in p.finditer(linha):
            print(match.group())
            f.write(match.group() + '\n')

f.close()
