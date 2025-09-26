import pygame
#Camera Inicial
cam_c = 0
cam_l = 0

cam_velocidade = 1

#Movimentação pelo teclado
def cam_mov(teclas, cam_coluna, cam_linha):
    
    if teclas[pygame.K_LEFT]:
        cam_coluna -= cam_velocidade
    if teclas[pygame.K_RIGHT]:
        cam_coluna += cam_velocidade
    if teclas[pygame.K_UP]:
        cam_linha -= cam_velocidade
    if teclas[pygame.K_DOWN]:
        cam_linha += cam_velocidade

    return cam_coluna, cam_linha



