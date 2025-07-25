a = ['maçã', 'laranja', 'cenoura', 'laranja', 'pera', 'maçã']
print(a)
print(len(a))
print(set(a))
print(len(set(a)))

b = ['laranja', 'pera', 'cenoura', 'batata', 'batata']
print(b)
print(len(b))
print(set(b))
print(len(set(b)))

set(a)
set(b)

# quais os elementos que estão tanto no A como no B? - interseção
print(set(a) & set(b))
print(set(a).intersection(b))
print(len(set(a).intersection(b)))
print(len(set(a) & set(b)))

# SETS Literais
meu_set = {1, 2}
print(meu_set)
meu_set.remove(1)
print(meu_set)
meu_set.add(3)
print(meu_set)
meu_set.pop() # retira o último valor
print(meu_set)
meu_set.pop # set-vazio
print(meu_set)

meu_set
print(meu_set) # o set fica vazio set()
