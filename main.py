#Importações
import pygame
from config import largura_tela, altura_tela, mapa_coluna, mapa_linha
from camera import cam_c, cam_l, cam_mov
from mapa import criar_mapa, desenhar_mapa
from npc import campones
     
#Execução do programa
def main():
    
    #Parametrôs de inicialização 
    pygame.init()
    pygame.display.set_caption("Vila I.A")
    
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    clock = pygame.time.Clock()
    mapa = criar_mapa(mapa_coluna, mapa_linha)
    npc_campones = campones(5, 5)
    cam_coluna = cam_c
    cam_linha = cam_l

    #Loop de Execução Global
    loop = True
    while loop:

        #Checa os eventos
        for eventos in pygame.event.get():
            
            
            #Camera
            teclas = pygame.key.get_pressed()
            cam_coluna, cam_linha = cam_mov(teclas, cam_coluna, cam_linha)
       
            #Fechando o Loop
            if eventos.type == pygame.QUIT:
                loop = False

        #Mapa
        desenhar_mapa(tela, mapa, cam_coluna, cam_linha, mapa_coluna, mapa_linha)
        
        #Npc
        npc_campones.mover(teclas)
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
    













