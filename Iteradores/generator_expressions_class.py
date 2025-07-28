dados = 'ralos'
print(list((dados [i] for i in range(len(dados)-1, -1, -1))))

print(sum(i*10 for i in range(10)))

vetor_x = [10, 20, 30]
vetor_y = [7, 5, 3]

print(sum((x*y for x,y in zip(vetor_x, vetor_y))))