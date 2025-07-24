# Default Values
# São valores atribuídos aos parâmetros de um método (ou função) caso esses
# parâmetros não sejam fornecidos quando o método é chamado

class Retangulo:
    def __init__(self, altura = None, largura = None):
        self.altura = altura
        self.largura = largura

ret1 = Retangulo()
ret2 = Retangulo()

ret1.largura = 12
print(ret1.largura)

# Na class Quadrado os valores da altura e largura são passados de forma default, o que faz
# com que o valor da área não seja alterável. MAS para que este se torne alterável consoante
# a alteração dos valores dos atributos. 
# Assim, a utilização do @property transforma a área numa propriedade e pode ser alterável os valores
class Quadrado:
    def __init__(self, altura = 10, largura = 20):
        self.altura = altura
        self.largura = largura

    @property    
    def area(self):
        return self.largura * self.altura
        
qua1 = Quadrado()
qua2 = Quadrado()

print(qua1.largura)
print(qua1.altura)
print(qua1.area)
 
qua1.altura = 30
qua1.largura = 30
print(qua1.area)

# Na class Pessoa, não há a necessidade de tornar os valores alteráveis porque estes valores
# são passados só quando o objeto é criado e os valores são passados nesse momento. 
class Pessoa:
    def __init__(self, nome, ano_nasc, ano_atual):
        self.nome = nome
        self.idade = ano_atual - ano_nasc

pedrinho = Pessoa('pedrinho', 1978, 2020)
print(pedrinho.idade)