#Blibiotecas
import pygame

#Funções - Temporiamente vou fazer no mesmo arquivo

#Grid visual
def grid_visual(tela):
    
    #Configurações da grid
    altura = 1280
    largura = 680
    tamanho_da_celula = 5
    colunas = altura//tamanho_da_celula
    linhas = largura//tamanho_da_celula
    
    #Cores
    fundo = (30,30,30) 
    cor_da_grid = (100,100,100)

    #Execução
    tela.fill(fundo)
    for x in range(0, altura, tamanho_da_celula):
        pygame.draw.line(tela, cor_da_grid, (x, 0), (x, largura))
    for y in range(0, largura, tamanho_da_celula):
        pygame.draw.line(tela, cor_da_grid, (0, y), (altura, y))
        
#Ececução do programa
def main():
    
    #Start e Parâtros da Janela
    pygame.init()

    tela = pygame.display.set_mode((1280,680)) #Tamanho da Tela       
    pygame.display.set_caption("Vila I.A.")   #Nome Provisório

    #Loop de Execução Global
    loop = True

    while loop:

        #Eventos
        for eventos in pygame.event.get():

            #Fechando o Aplicativo
            if eventos.type == pygame.QUIT:
                loop = False
                
        grid_visual(tela) #Mostrar a grid
        pygame.display.flip()
        
    pygame.quit()

#Iniciar Programa
main()










