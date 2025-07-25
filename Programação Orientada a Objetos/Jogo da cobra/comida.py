import random
# fazer import da biblioteca random para poder gerar uma posição aleatória para a comida

class Comida:
    def __init__(self, tam_tela=(300, 400)):
        self.tam_tela = tam_tela
        # a posição da comida tem de ser aleatória
        self.posicao = [random.randrange(10, self.tam_tela[0], 10), 
                        random.randrange(10, self.tam_tela[1], 10)]
        # se ja foi comida ou nao
        self.devorada = False
    
    def gera_nova_comida(self):
        if self.devorada:
            # a posição da comida tem de ser aleatória
            self.posicao = [random.randrange(10, self.tam_tela[0], 10), 
                            random.randrange(10, self.tam_tela[1], 10)]
            self.devorada = False  
        return self.posicao