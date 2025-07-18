a = 3
print(a)  # atribuição de valor a variável a

b = 2
print(b)  # atribuição de valor a variável b
print(a+b)

c = '3'
#print(b+c) # concatenação de string com número dá erro porque não é possível somar str com int

d = '4'
print(c+d)  # concatenação de strings, neste caso não dá erro porque são ambos strings

print(type(a))  # tipo da variável a

int(c) # converte a string c para inteiro
str(b) # converte o inteiro b para string

variable_name_with_underscore = 5  # o nome da variável separa-se com underscore


# variáveis não são caixas
# fibonacci
# 0 1 1 2 3 5 8 13 21 ... 
# é a soma dos dois valores anteriores ao que eu estou a escrever
fibo = [0,1]
fibo.append(fibo[-2]+ fibo[-1])  # adiciona o próximo valor da sequência de Fibonacci
print(fibo)  # imprime a sequência de Fibonacci até o terceiro elemento