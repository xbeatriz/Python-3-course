# Iteradores / Iterators

for elemento in [1,2,3]:
    print(elemento)

for elemento in (1,2,3):
    print(elemento)

for elemento in {'um': 1, 'dois': 2, 'tres': 3}:
    print(elemento)

for elemento in '123':
    print(elemento)

# O estilo de acessar o loop é claro, consiso e conveniente. O uso de iterators ajudam a unificar o Python. 
# O que o for faz por de trás é chamar o iter(). A função retorna um objeto iterador que define o método __next__() que acessa os elementos um por um. 
# Quando não existe mais elementos, __next__() faz um raise da exceção StopIteration que fala para o loop do for encerrar
# Podemos chamar o método __next__() usando a função next() built-in;

s = 'abc'
iterador = iter(s)
print(iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))


# LOOP INVERTIDO
class Inverso:
    """Iterador para realizar loops de trás para frente"""
    def __init__(self, dados):
        self.dados = dados
        self.index = len(dados)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.dados[self.index]
    
inv = Inverso('folha')
print(inv)

for elemento in inv:
    print(elemento)