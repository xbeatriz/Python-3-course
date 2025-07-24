class Computador: 
    pass 

# Aqui criamos 3 objetos da  classe computador
pc1 = Computador()  # Instância da classe Computador
print(type(pc1))  # Imprime o tipo da instância pc1 
pc2 = Computador()  # Outra instância da classe Computador
print(type(pc2))  # Imprime o tipo da instância pc2
pc3 = Computador()  # Mais uma instância da classe Computador
print(type(pc3))  # Imprime o tipo da instância pc3

# Aqui atribuímos atributos aos objetos criados
pc1.cor = 'preto'  # Atribui a cor 'preto' à instância pc1
pc2.cor = 'branco'  # Atribui a cor 'branco' à instância pc2
pc3.cor = 'prata'  # Atribui a cor 'prata'

print(pc1.cor)  # Imprime a cor da instância pc1
print(pc2.cor)  # Imprime a cor da instância pc2
print(pc3.cor)  # Imprime a cor da instância pc3

pc1.hd = 500
pc2.hd = 1000
pc3.hd = 350

print(pc1.hd)  # Imprime o HD da instância pc1
print(pc2.hd)  # Imprime o HD da instância pc2
print(pc3.hd)  # Imprime o HD da instância pc3

class Retangulo:
    pass

ret1 = Retangulo()  # Instância da classe Retangulo
ret2 = Retangulo()  # Outra instância da classe Retangulo

ret1.altura = 20 
ret2.altura = 10

ret1.largura = 30
ret2.largura = 15

print(ret1.altura * ret1.largura)  # Imprime a área do retângulo ret1
print(ret2.altura * ret2.largura)  # Imprime a área do retângulo ret2


###### __init__ e self ######
class Notebook:
    def __init__(self, cor, hd): # quando colocamos self - proprio objeto - é como se estivéssemos dizendo que o objeto Notebook tem esses atributos
        self.cor = cor
        self.hd = hd

pc1 = Notebook('preto', 500)
pc2 = Notebook('branco', 1000)
pc3 = Notebook('prata', 350)

print(pc1, pc2, pc3)  # Imprime as instâncias dos notebooks

