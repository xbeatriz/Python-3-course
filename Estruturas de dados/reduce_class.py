###### reduce #######
# Função reduce aplica uma função cumulativa aos elementos de um iterável, reduzindo-o a um único valor.

from functools import reduce  # Importa a função reduce do módulo functools

numeros = list(range(1, 11))  # Create a list of numbers from 1 to 10
print(numeros)  # Print the list of numbers

print(sum(numeros))  # Print the sum of the numbers

def soma(x, y):  # Define a function that sums two numbers
    return x + y  # Return the sum of x and y

reduce(soma, numeros)  # Apply the soma function cumulatively to the list of numbers
print(reduce(soma, numeros))  # Print the result of the reduce function

def multiplica(x, y):  # Define a function that multiplies two numbers
    return x * y  # Return the product of x and y

print(reduce(multiplica, numeros))  # Print the result of the reduce function with multiplication


print(reduce(lambda x, y: x * y, numeros))  # Print the result

# for 
produto = 1
for x in numeros: # Iterate through the list of numbers
    produto = produto * x  # Multiply each number to the product
    # produto *= x

print(produto)  # Print the final product