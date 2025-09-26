import pygame
from config import tamanho_da_celula

class campones:
    def __init__(self, x, y):

        #Posição
        self.x = x
        self.y = y

        #Hitbox
        self.largura = tamanho_da_celula
        self.altura = tamanho_da_celula * 2
        self.cor = (0, 0, 255)

        #Velocidade
        self.velocidade = 1

        #

    def mover(self, teclas):

        if teclas[pygame.K_w]:
            self.y -= self.velocidade
                    
        if teclas[pygame.K_s]:
            self.y += self.velocidade
                   
        if teclas[pygame.K_a]:
            self.x -= self.velocidade
                    
        if teclas[pygame.K_d]:
            self.x += self.velocidade

    def desenhar(self, tela, cam_coluna, cam_linha):

        #Posicão[x][y] para pixels na tela
        x = (self.x - cam_coluna) * tamanho_da_celula
        y = (self.y - cam_linha) * tamanho_da_celula - (self.altura - tamanho_da_celula)
    
        #Janela rect e desenho
        rect = pygame.Rect(x, y, self.largura, self.altura)
        pygame.draw.rect(tela, self.cor, rect)
