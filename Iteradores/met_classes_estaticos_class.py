class Funcionario():
    aumento = 1.04
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
        
    @classmethod
    def definir_aumento(cls, aumento):
        cls.aumento = aumento
    
    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return 'Dia útil'
        return True

fabio = Funcionario('Fabio', 7000)
print(fabio.dados())
fabio.aplicar_aumento()
print(fabio.dados())
Funcionario.definir_aumento(1.05)
pedro = Funcionario('Pedro', 8000)
pedro.aplicar_aumento()
print(pedro.dados())

import datetime

minha_data = datetime.date(2019, 4, 11)
print(Funcionario.dia_util(minha_data))