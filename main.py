#Blibiotecas
import pygame

#Configurações da Janela
altura_tela = 1280
largura_tela = 680
tamanho_da_celula = 20

#Configurações do Mapa
mapa_coluna = 100
mapa_linhas = 100

#Cores
fundo = (30,30,30) 
cor_da_grade = (100,100,100)
cor_obstaculo = (180, 60, 60)
cor_debug = (200, 200, 50)

#Mapa
def criar_mapa(colunas,linhas):
    
    grid = [[ 0 for x in range(colunas)] for y in range(linhas)]

    #Futuras Criações de estruturas, reservar valores e alterar de zero para 1: Obstaculo
    

#Visual    
def desenhar_mapa(tela, grid, cam_coluna, cam_linha)
                        
        
#Execução do programa
def main():
    
    #Start e Parâtros 
    pygame.init()
    pygame.display.set_caption("Path Neural")   #Nome Provisório
    
    tela = pygame.display.set_mode((1280,680)) #Tamanho da Tela        
    
    grid = criar_mapa(mapa_coluna, mapa_linha)
    cam_coluna = 0
    cam_linha = 0

    #Loop de Execução Global
    loop = True

    while loop:

        #Eventos
        for eventos in pygame.event.get():

            #Fechando o Aplicativo
            if eventos.type == pygame.QUIT:
                loop = False


        desenhar_mapa(tela, grid, cam_coluna, cam,linha)
        pygame.display.flip() 

    pygame.quit()

#Iniciar Programa
main()













