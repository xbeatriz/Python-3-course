# Sobrecarga de operadores

class Numero:
    def __init__(self, num):
        self.num = num

    # adicionar um novo método na função
    def __add__(self, outro):
        return int(str(self.num) + str(outro.num)) #transforma os numeros em string, mas o tipo de resultado sera um int
    
    # vai alterar a forma como é representado o N1, e o N2
    def __repr__(self):
        return f'Numero {self.num}'
    
    def __eq__(self, outro):
        return self.num == outro.num

n1 = Numero(2)
n2 = Numero(2)
print(n1, n2)

n3 = n1 + n2

# n1 + n2 - vai dar um erro de que não é suportado por serem valores vindos de uma classe que eu nao coloquei regra (1ª tentativa)

print(n3)
print(n3 - 10)
