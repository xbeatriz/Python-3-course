# diferentes maneiras de se criar um dicionário

a = {'um': 1, 'dois': 2, 'três': 3}
print(a)

b = dict(um=1, dois=2, três=3)
print(b)

c = dict(zip(['três', 'dois', 'um'], [3, 2, 1]))
print(c)

d = dict([('dois', 2), ('um', 1), ('três', 3)])
print(d)

print(a == b == c == d)


