# composição => parte de 
# Composição é quando uma classe tem objetos de outras classes como atributos.
# herança "É um" - Um Cachorro é um Animal
# != 
# Composição "Tem um " - Um Carro tem um Motor

class Endereco:
    def __init__(self, codigo_postal, rua = None, numero = None, casa = None, bairro = None, cidade = None):
        self.codigo_postal = codigo_postal
        self.rua = rua
        self.numero = numero
        self.casa = casa
        self.bairro = bairro
        self.cidade = cidade 

class Pessoa:
    def __init__(self, nome, idade, email, *args, **kwargs):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.obj_endereco = Endereco(*args, **kwargs) # é um objeto desta class

ana = Pessoa('ana', 28, 'ana@email.com', 4760.777)
print(ana.obj_endereco.codigo_postal)

# livro > capítulos
# casa > telhado, parede, etc...
# carro > pneus, voltante, banco, janelas...
# computador > teclado, mouse, monitor, etc...

# Ou seja na herança, eu digo Um gerente é uma pessoa, um Gerente é um Funcionario
# mas na composição eu digo que uma Casa TEM um telhado, tem paredes. Ou um Carro tem Pneus, Vidros....
