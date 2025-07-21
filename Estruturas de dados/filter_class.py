########## filter ########
# filter é uma função que recebe dois argumentos: uma função e um iterável (como uma lista, tupla, etc.).
# Ela aplica a função a cada item do iterável e retorna um iterável contendo apenas os itens para os quais a função retornou True.

numeros = list(range(1, 11))  # Create a list of numbers from 1 to 10
print(numeros)  # Print the list of numbers

filter(lambda x: x > 5, numeros)  # Filter numbers greater than 5
print(list(filter(lambda x: x > 5, numeros)))  # Convert the filter object to a list and print it

# compreensão de listas
[x for x in numeros if x > 5]  # List comprehension to filter numbers greater than 5
print([x for x in numeros if x > 5])  # Print the filtered list

dados = ['', 'b', 'c', '', '', 'f', 'h', 'i', 'j']  # List with some empty strings
print(dados)  # Print the list with empty strings
# Filter out empty strings from the list
print(list(filter(None, dados)))  # Print the filtered list without empty strings

def vazio(x):
    if x == '':
        return True  # Return True if the string is empty
    return False  # Return False if the string is not empty
print(list(filter(vazio, dados)))  # Print the filtered list using the vazio function

# compreensão de listas para filtrar vazios
print([x for x in dados if x != ''])  # List comprehension to filter out empty strings