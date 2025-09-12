import pygame
from config import largura_tela, altura_tela, tamanho_da_celula
from config import fundo, cor_da_grade, cor_debug

#Mapa
def criar_mapa(linhas,colunas):
    grid = [[ 0 for x in range(colunas)] for y in range(linhas)]
    
    #Futuras Criações de estruturas, reservar valores e alterar de zero para 1: Obstaculo
    #grid[0][0] = 1 debub - excluir depois
    
    return grid

#Desenhando    
def desenhar_mapa(tela, grid, cam_coluna, cam_linha, mapa_coluna, mapa_linha):
    
    tela.fill(fundo)

    quant_colunas = largura_tela // tamanho_da_celula
    quant_linhas = altura_tela // tamanho_da_celula
      
    #Varrendo toda a janela e guardando em coordenadas
    for x_coluna in range(quant_colunas):
        for y_linha in range(quant_linhas):
            janela_atual_coluna = cam_coluna + x_coluna
            janela_atual_linha = cam_linha + y_linha

            #Verificando se a janela está dentro do mapa
            if (0 <= janela_atual_coluna < mapa_linha and 0 <= janela_atual_linha < mapa_coluna):

                #Formação da janela atual em notação da grade matemática
                janela_atual_coordenada = grid[janela_atual_coluna][janela_atual_linha]

                #Criando a janela pela função rect para possibilitar o desenho
                celula_x = x_coluna * tamanho_da_celula
                celula_y = y_linha * tamanho_da_celula
                rect = pygame.Rect(celula_x, celula_y, tamanho_da_celula, tamanho_da_celula)

                #Desenhando de acordo com valor
                if janela_atual_coordenada == 0:
                    pygame.draw.rect(tela, fundo, rect)
                elif janela_atual_coordenada == 1: #Debug
                    pygame.draw.rect(tela, cor_debug, rect)

                #Desenhando a grade
                pygame.draw.rect(tela, cor_da_grade, rect, 1)
