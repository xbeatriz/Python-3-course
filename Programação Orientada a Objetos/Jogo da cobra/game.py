# pip install pygame

import pygame
import sys
from snake import Cobra # importação da Class Cobra do ficheiro snake.py
from comida import Comida # importação da Class Comida do ficheiro comida.py
import time

# iniciar a fonte
pygame.font.init()
minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)

# inicializar o pygame
pygame.init()
TAM_TELA = (300, 400)
tela = pygame.display.set_mode(TAM_TELA)

# cronometro | tempo
tempo = pygame.time.Clock()

pontuacao = 0

cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao

# iniciar o loop do jogo
while True: 

    tela.fill((7,0,35)) # RGB - red green blue
    for event in pygame.event.get():
        # listener - mouse ou teclado
        if event.type == pygame.QUIT:
            # interrompe o pygame
            pygame.quit()
            # fechar script (janela)
            sys.exit()
        
        # se alguma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cobra.muda_direcao('DIREITA')
            if event.key == pygame.K_LEFT:
                cobra.muda_direcao('ESQUERDA')
            if event.key == pygame.K_DOWN:
                cobra.muda_direcao('BAIXO')
            if event.key == pygame.K_UP:
                cobra.muda_direcao('CIMA')

    posicao_comida = comida.gera_nova_comida()
    # se a cobra comeu a comida
    if cobra.move(posicao_comida):
        comida.devorada = True
        pontuacao +=  1
    
    if cobra.verifica_colisao():
        pontos = minha_fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
        tela.blit(pontos, (10, 10))
        voce_perdeu = minha_fonte.render('TU PERDESTE!', True, (255, 255, 255))
        tela.blit(voce_perdeu, (80, 180))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # texto da pontuacao
    pontos = minha_fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
    tela.blit(pontos, (10, 10))

    # desenha cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255,204,0),
                         # esquerda, cima, largura, altura
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # desenha comida
    pygame.draw.rect(tela, pygame.Color(255,0,0),
                     pygame.Rect(posicao_comida[0], posicao_comida[1], 10, 10 ))


    # atualiza a tela a cada frame       
    pygame.display.update()

    # FPS - frames por segundo
    tempo.tick(20)

