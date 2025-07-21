##### map #####
# This code demonstrates the use of the map function to apply a function to each item in an iterable.

numeros = list(range(1, 11))  # Create a list of numbers from 1 to 10
print(numeros)  # Print the list of numbers

def quadrado(x):
    return x ** 2  # Function to calculate the square of a number

map (quadrado, numeros)  # Apply the quadrado function to each item in numeros
# map com função
print(list(map(quadrado, numeros)))  # Convert the map object to a list and print it

#map com lambda
# Using a lambda function to achieve the same result
print(list(map(lambda x: x ** 2, numeros)))  # Print the list of squared numbers

# compreensão de listas
[x**2 for x in numeros]  # List comprehension to calculate squares
print([x**2 for x in numeros])  # Print the list of squared numbers

# for normal
nova_lista = []  # Initialize an empty list
for x in numeros:
    nova_lista.append(x**2)

print(nova_lista)  # Print the list of squared numbers



