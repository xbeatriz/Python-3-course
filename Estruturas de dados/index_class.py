# Indexing and Slicing Strings

palavra = "python"

palavra[0] # output: 'p'
palavra[-1] # o último caracter
palavra[-2] # o penúltimo caracter

#Slicing
palavra[0:2] # output: 'py' (do índice 0 até o índice 2, sem incluir o índice 2)
palavra[:2] # todos os caracteres até ao 2
palavra[2:] # todos os caracteres do 2 até ao final
palavra[:1] + palavra[1:]
# As strings são imutáveis, não é possível alterar um caracter diretamente
palavra[1] = 'ai' # isso gera um erro

s = 'minhastringcomumapalavrasupergrande'
len(s) # conta os caracteres todos da string

