# === Operadores de Comparação ===
a = 10
b = 5

print("== Operadores de Comparação ==")
print("a == b:", a == b)     # False verifica se a é igual a b
print("a != b:", a != b)     # True verifica se a é diferente de b
print("a > b:", a > b)       # True verifica se a é maior que b
print("a < b:", a < b)       # False verifica se a é menor que b
print("a >= b:", a >= b)     # True verifica se a é maior ou igual a b
print("a <= b:", a <= b)     # False verifica se a é menor ou igual a b
print()

# === Operadores Lógicos ===
x = True
y = False

print("== Operadores Lógicos ==")
print("x and y:", x and y)   # False verifica se ambos são verdadeiros
print("x or y:", x or y)     # True verifica se pelo menos um é verdadeiro
print("not x:", not x)       # False inverte o valor de x
print()

# Operadores lógicos combinando comparações
idade = 25
tem_carteira = True

print("Pode conduzir?", idade >= 18 and tem_carteira)  # True verifica se a pessoa tem idade suficiente e carteira de motorista
print()

# === Operadores Bit a Bit (Bitwise) ===
m = 6   # bin: 0110
n = 3   # bin: 0011

print("== Operadores Bit a Bit ==")
print("m & n (AND):", m & n)     # 2 (bin: 0010) verifica se ambos os bits são 1
print("m | n (OR):", m | n)     # 7 (bin: 0111) verifica se pelo menos um dos bits é 1
print("m ^ n (XOR):", m ^ n)    # 5 (bin: 0101) verifica se os bits são diferentes
print("~m (NOT):", ~m)          # -7 (complemento de 2) inverte todos os bits de m
print("m << 1 (shift esq):", m << 1)  # 12 (bin: 1100) desloca os bits de m para a esquerda
print("m >> 1 (shift dir):", m >> 1)  # 3 (bin: 0011) desloca os bits de m para a direita
