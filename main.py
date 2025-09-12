#Blibiotecas
import pygame
from config import largura_tela, altura_tela, mapa_coluna, mapa_linha
from mapa import criar_mapa, desenhar_mapa
     
#Execução do programa
def main():
    
    #Start e Parâmetros 
    pygame.init()

    #fps
    clock = pygame.time.Clock()

    #Nome Provisório
    pygame.display.set_caption("Path Neural")   

    #Tamanho da Tela
    tela = pygame.display.set_mode((largura_tela, altura_tela))         

    
    grid = criar_mapa(mapa_coluna, mapa_linha)

    #Camera
    cam_linha = 0
    cam_coluna = 0

    #Loop de Execução Global
    loop = True

    while loop:

        #Eventos
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
                
            #Fechando o Aplicativo
            if eventos.type == pygame.QUIT:
                loop = False


        desenhar_mapa(tela, grid, cam_coluna, cam_linha, mapa_coluna, mapa_linha)
        clock.tick(60)
        pygame.display.flip() 

    pygame.quit()

#Iniciar Programa
if __name__ == "__main__":
    main()













