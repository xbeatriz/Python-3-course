# Encapsulamento - getters e setters
# Encapsulamento é o princípio de esconder os detalhes internos de uma classe e
# permitir o acesso a essas dados apenas através de métodos públicos controlados
# basicamente serve para proteger os dados da classe para que não sejam modificados diretamente de fora

# getter & setters
# são métodos especiais que permitem aceder (getter) ou modificar (setter) um atributo de forma controlada
# getter - método para ler um atributo privado
# setter - método para modificar um atributo prinvado

# public, private, etc...
# Nesta classe temos três atributos, cada um com um nivel diferente de privacidade
class Fixa: 
    def __init__(self):
        self.publico = 'publico' # pode ser acedido diretamente fora da classe
        self._privado_por_convencao = ' privado por conveção' # _ este é para uso interno e pode ser mexido
        self.__privado_mesmo = 'privado mesmo' # __ esconde o nome do atributo automaticamente para evitar acesso direto acidental
        
    def get_publico(self):
        return self.publico
    
    def set_publico(self, valor):
        self.publico = valor

    def get_privado_por_convencao(self):
        return self._privado_por_convencao
    
    def get_privado_mesmo(self):
        return self.__privado_mesmo
fixa = Fixa()

print(fixa.publico)
print(fixa._privado_por_convencao)
# print(fixa.__privado_mesmo) - vai dar erro porque não vai passar porque ele é privado

# exemplo da classe computador
class Computador:
    def __init__(self, cor, hd):
        self.__cor = cor
        self.__hd = hd
    
    def get_cor(self): # desta forma eu consigo acessar ao atributo cor fora da class
        return self.__cor
    
    def set_cor(self, valor):
        self.__cor = valor
    
pc1 = Computador('preto', 500)
print(pc1.get_cor())
pc1.set_cor('branco')
print(pc1.get_cor())

