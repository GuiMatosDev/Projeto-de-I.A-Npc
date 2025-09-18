#Importações
import pygame
from config import largura_tela, altura_tela, mapa_coluna, mapa_linha
from mapa import criar_mapa, desenhar_mapa
from npc import campones
     
#Execução do programa
def main():
    
    #Start 
    pygame.init()

    #Nome provisório
    pygame.display.set_caption("Path Neural")

    #Janela
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    #Fps
    clock = pygame.time.Clock()

    #Grade matemática
    mapa = criar_mapa(mapa_coluna, mapa_linha)

    #Npc
    npc_campones = campones(5, 5) 

    #Camera
    cam_linha = 0
    cam_coluna = 0

    #Loop de Execução Global
    loop = True
    while loop:

        #Checa os eventos
        for eventos in pygame.event.get():

            #Movimento da Camera pelo teclado
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                cam_coluna = cam_coluna - 1
            if teclas[pygame.K_RIGHT]:
                cam_coluna = cam_coluna + 1
            if teclas[pygame.K_UP]:
                cam_linha = cam_linha - 1
            if teclas[pygame.K_DOWN]:
                cam_linha = cam_linha + 1
                
            #Fechando o Loop
            if eventos.type == pygame.QUIT:
                loop = False

        #Desenha o mapa
        desenhar_mapa(tela, mapa, cam_coluna, cam_linha, mapa_coluna, mapa_linha)

        #Desenha o npc
        npc_campones.desenhar(tela, cam_coluna, cam_linha)

        #Fps
        clock.tick(60)

        #Executa o que foi processado
        pygame.display.flip() 

    #Fechando o Aplicativo
    pygame.quit()

#Iniciar Programa
if __name__ == "__main__":
    main()













