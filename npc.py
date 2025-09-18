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
        

    def desenhar(self, tela, cam_coluna, cam_linha):

        #Posicão para pixels
        p_x = self.x - cam_coluna
        p_y = self.y - cam_linha
    
        screen_x = p_x * tamanho_da_celula
        screen_y = p_y * tamanho_da_celula - (self.altura - tamanho_da_celula)


        #Janela rect e desenho
        rect = pygame.Rect(screen_x, screen_y, self.largura, self.altura)
        pygame.draw.rect(tela, self.cor, rect)
