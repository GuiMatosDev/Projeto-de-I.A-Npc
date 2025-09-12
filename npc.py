import pygame
from config import tamanho_da_celula

class npc_campones:
    def __init__(self, x_coluna, y_linha):

        #Posição
        self.x = x_coluna
        self.y = y_linha

        #Visual do personagem (temporáriamente: retângulo)
        largura = tamanho_da_celula
        altura = tamanho_da_celula * 2
        self.cor = (0, 0, 255)
        

    def desenhar(self, tela):

        #Posicão -> pixels
        x = self.x * tamanho_da_celula
        y = self.y * tamanho_da_celula - (self.altura - tamanho_da_celula)

        #Janela rect e desenho
        rect = pygame.Rect(x, y, largura, altura)
        pygame.draw.rect(tela, self.cor, rect)
