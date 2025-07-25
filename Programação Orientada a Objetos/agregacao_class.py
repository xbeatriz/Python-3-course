# Agregação - possui um(a)
# é um tipo especial de composição, com uma diferença importante:
# composição forte - a parte não vive sem o todo
# agregação (composição fraca) - a parte  pode existir sozinha
# a agregação é uma relação "possui um(a)", mas onde os objetos têm vidas independentes

# composição - Um Carro tem um Motor
# agregação - Um Professor possui uma escola (mas vive sem ela)

class Endereco:
    def __init__(self, codigo_postal, rua = None, numero = None, casa = None, bairro = None, cidade = None):
        self.codigo_postal = codigo_postal
        self.rua = rua
        self.numero = numero
        self.casa = casa
        self.bairro = bairro
        self.cidade = cidade 

class Pessoa:
    def __init__(self, nome, idade, email, endereco):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.obj_endereco = endereco

ana_end = Endereco(61526272)
ana = Pessoa('ana', 28, 'ana@email.com', ana_end)
print(ana)
