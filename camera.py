import pygame
#Camera Inicial
cam_c = 0
cam_l = 0

#Movimentação pelo teclado
def cam_mov(teclas, cam_coluna, cam_linha):
    
    if teclas[pygame.K_LEFT]:
        cam_coluna -= 1
    if teclas[pygame.K_RIGHT]:
        cam_coluna += 1
    if teclas[pygame.K_UP]:
        cam_linha -= 1
    if teclas[pygame.K_DOWN]:
        cam_linha += 1

    return cam_coluna, cam_linha



