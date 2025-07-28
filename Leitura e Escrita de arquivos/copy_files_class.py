# copiar arquivos de texto

with open('Leitura e Escrita de arquivos/meu_arquivo.txt', 'r') as meu_arquivo:
    with open('Leitura e Escrita de arquivos/meu_arq_copia.txt', 'w') as meu_arq_copia:
        for linha in meu_arquivo: 
            meu_arq_copia.write(linha)