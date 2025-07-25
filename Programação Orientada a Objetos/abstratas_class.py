# Classes Abstratas
# uma classe abstrata é uma classe que serve de modelo para outras classes.
# Além disso, ela não pode ser instanciada e pode conter ou não métodos abstratos,
# podendo ser implementados nas classes descendentes

# Não pode ser instanciada
# É passada como herança
# Se possui métodos abstratos, estes devem ser implementaods nas classes descendentes
# Pode conter ou não métodos abstratos

# métodos abstratos >> são métodos que precisam ser implementados nas classes descendentes

""" class Abstrata:
    def metodo_abstrato(self):
        pass
    
    def metodo_nao_abstrato(self):
        pass

class Descendente(Abstrata):
    def __init__(self, nome):
        self.nome = nome

abstrata = Abstrata()
print(abstrata)

desc = Descendente('descendente')
print(desc) """

# Abstract Base Classes
from abc import ABC, abstractmethod

class Abstrata(ABC):

    @abstractmethod
    def metodo_abstrato(self):
        pass

    def metodo_nao_abstrato(self):
        pass

    @abstractmethod
    def outro_metodo_abstrato(self):
        pass

# bstrata = Abstrata() Não dá para instanciar abstract classes sempre implementação dos metodos abstratos. 

class Descendente(Abstrata):
    def __init__(self, nome):
        self.nome = nome

    def metodo_abstrato(self):
        print('Metodo abstrato implementado')

    def outro_metodo_abstrato(self):
        print('outro metodo abstrato implementado')

desc = Descendente('descendente')

desc.metodo_abstrato()