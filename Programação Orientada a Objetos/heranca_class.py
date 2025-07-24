# Herança - classes e sub classes 
# Permite que uma classe herde atributos e métodos de outra classe
# Classe - animal
# subclasse - gato, cachorro, elefante, etc...

class Animal:
    pass

class Gato(Animal):
    pass



class Poligono:
    __largura = None
    __altura = None

    def set_valores(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def get_largura(self):
        return self.__largura
    
    def set_largura(self, valor):
        self.__largura = valor

    def get_altura(self):
        return self.__altura
    
    def set_altura(self, valor):
        self.__altura = valor

class Retangulo(Poligono):
    def get_area(self):
        return self.get_largura() * self.get_altura()

class Triangulo(Poligono):
    def get_area(self):
        return self.get_largura() * self.get_altura() / 2

ret = Retangulo()
tri = Triangulo()


ret.set_valores(2,3)
tri.set_valores(5,2)

print(ret.get_area())
print(tri.get_area())


###### Heranças múltiplas

class Pessoa:
    pass

class Funcionario:
    pass

class Gerente(Funcionario, Pessoa):
    pass

##### super()

class Pai1:
    def __init__(self):
        print('__init__Pai1')

class Pai2:
    def __init__(self):
        print('__init__Pai2')

class Filho(Pai1):
    def __init__(self):
        print('__init__Filho') # se so tiver este so vai imprimir o da class filho
        super().__init__() # desta forma imprime tambem o que está presente na superclasse Pai1

class Filho2(Pai1, Pai2):
    def __init__(self):
        print('__init__Filho2')
        Pai1.__init__(self)
        Pai2.__init__(self)

filho = Filho()
filho2 = Filho2()

# __mro__ = method resolution order - é a ordem que os métodos são chamados
print(Filho.__mro__)
