import pygame
from config import cor_personagem

class npc_campones:
    def __init__(self, x, y, cor_personagem):

        #Parâmetros Básicos 
        self.x = x
        self.y = y
        self.cor = cor_personagem
        self.velocidade = 1

    def desenhar(self, tela, tamanho_da_celula):

        #Desenho
        pygame.draw.rect(

            #Parametrôs para a criação do desenho pelo rect
            tela,
            self.cor_personagem,
            (
                self.x * tamanho_da_celula, #X
                self.y * tamanho_da_celula, #Y
                tamanho_da_celula,          #Largura
                tamanho_da_celula           #Altura
            )
        )

    def mover(self, direcao_x, direcao_y , grid, colisoes):

        #Proxima posição
        novo_x = self.x + direcao_x *  
        novo_y = self.y

