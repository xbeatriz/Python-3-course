import requests

class Funcionario:
    aumento = 1.10

    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    @property
    def nome_completo(self):
        return  f'{self.nome} {self.sobrenome}'

    @property
    def email(self):
        return f'{self.nome}.{self.sobrenome}@email.com'.lower()

    def aplica_aumento(self):
        self.salario = self.salario * self.aumento

    def pagina(self):
        resposta = requests.get(f'https://empresa.com/{self.nome}-{self.sobrenome}'.lower())
        if resposta.ok:
            return resposta.text
        else:
            return 'Má requisição!'
