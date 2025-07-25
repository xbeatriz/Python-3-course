class Cobra: 
    def __init__(self, tam_tel=(300,400),
                 posicao = [80, 50], # esquerda, cima
                 corpo = [[80, 50], [70, 50], [60, 50]],
                 direcao = 'DIREITA'):
        
        self.tam_tel = tam_tel
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = direcao
    
    # comandos para a minhoca andar
    def muda_direcao(self, nova_direcao):
        if nova_direcao == 'DIREITA' and not self.direcao == 'ESQUERDA' :
            self.direcao = 'DIREITA'
        if nova_direcao == 'ESQUERDA' and not self.direcao == 'DIREITA' :
            self.direcao = 'ESQUERDA'
        if nova_direcao == 'CIMA' and not self.direcao == 'BAIXO' :
            self.direcao = 'CIMA'
        if nova_direcao == 'BAIXO' and not self.direcao == 'CIMA' :
            self.direcao = 'BAIXO'
            

    def move(self, posicao_comida):
        if self.direcao == 'DIREITA':
            self.posicao[0] += 10
        if self.direcao == 'ESQUERDA':
            self.posicao[0] -= 10
        if self.direcao == 'CIMA':
            self.posicao[1] -= 10
        if self.direcao == 'BAIXO':
            self.posicao[1] += 10
        
        # adiciona pedaço do corpo da cobra na frente da cabeça
        self.corpo.insert(0, list(self.posicao))
        # confere se comeu comida
        if self.posicao == posicao_comida:
            return True
        # remove pedaço da parte de trás da cauda
        self.corpo.pop()
        return False

    def verifica_colisao(self):
        # posicao => [esquerda, cima]
        # tam_tela => [largura, altura]

        # se dist_esquerda > tam_tela_horizontal ou se a dist_esquerda < 0
        if self.posicao[0] > (self.tam_tel[0]-10) or self.posicao[0] < 0:
            return True
        
        # se dist_cima > tam_tela_vertical ou se a dist_baixo < 0
        if self.posicao[1] > (self.tam_tel[1]-10) or self.posicao[1] < 0:
            return True
        
        # verificar colisao com o proprio corpo
        for parte_do_corpo in self.corpo[1:]:
            if self.posicao == parte_do_corpo:
                return True