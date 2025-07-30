from math import pi

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Não pode dividir por zero")
    return a / b

def multiplica(a, b):
    """ multiplica a * b """
    return a * b

def subtrai(a, b):
    return a - b

def area_circulo(r):
    # pi*r²
    if r < 0:
        raise ValueError("Não é possível calcular área de raio negativo")
    return pi * (r**2)
