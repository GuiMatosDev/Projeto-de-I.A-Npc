#Blibiotecas
import pygame

#linha - altura
#coluna - largura

#Configurações da Janela
altura_tela = 1280
largura_tela = 680
tamanho_da_celula = 20

#Configurações do Mapa
mapa_linha = 100
mapa_coluna = 100


#Cores
fundo = (30,30,30) 
cor_da_grade = (100,100,100)
cor_obstaculo = (180, 60, 60)
cor_debug = (200, 200, 50)

#Mapa
def criar_mapa(linhas,colunas):
    
    grid = [[ 0 for y in range(linhas)] for x in range(colunas)]

    #Futuras Criações de estruturas, reservar valores e alterar de zero para 1: Obstaculo
    
    return grid

#Visual    
def desenhar_mapa(tela, grid, cam_linha, cam_coluna):
    
    tela.fill(fundo)

    quant_linhas = largura_tela // tamanho_da_celula
    quant_colunas = altura_tela // tamanho_da_celula
    
    
    #Varrendo toda a janela e guardando em coordenadas
    for y_linha in range(quant_linhas):
        for x_coluna in range(quant_colunas):
            mapa_linha_atual = cam_linha + y_linha
            mapa_coluna_atual = cam_coluna + x_coluna

            #Verifica se a célula está dentro do mapa
            if (0 <= mapa_linha_atual < mapa_linha and 0 <= mapa_coluna_atual < mapa_coluna):

                #
                valor = grid[mapa_linha_atual][mapa_coluna_atual]
                
                
        
#Execução do programa
def main():
    
    #Start e Parâtros 
    pygame.init()
    pygame.display.set_caption("Path Neural")   #Nome Provisório
    
    tela = pygame.display.set_mode((1280,680)) #Tamanho da Tela        
    
    grid = criar_mapa(mapa_linha, mapa_coluna)
    cam_linha = 0
    cam_coluna = 0
    

    #Loop de Execução Global
    loop = True

    while loop:

        #Eventos
        for eventos in pygame.event.get():

            #Fechando o Aplicativo
            if eventos.type == pygame.QUIT:
                loop = False


        desenhar_mapa(tela, grid, cam_linha, cam_coluna)
        pygame.display.flip() 

    pygame.quit()

#Iniciar Programa
main()













