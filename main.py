
#Blibiotecas
import pygame

#Variáveis Globais#
#Configurações
altura = 1280
largura = 680
tamanho_da_celula = 20
colunas = altura//tamanho_da_celula
linhas = largura//tamanho_da_celula
#Cores
fundo = (30,30,30) 
cor_da_grid = (100,100,100) 


def main():
    #Start e Parâtros da Janela
    pygame.init()
    tela = pygame.display.set_mode((altura,largura)) #Tamanho da Tela       
    pygame.display.set_caption("Vila I.A.")   #Nome Provisório

    #Loop de Execução Global
    loop = True

    while loop:

        #Eventos
        for eventos in pygame.event.get():

            #Fechando o Aplicativo
            if eventos.type == pygame.QUIT:
                loop = False
                
    pygame.quit()








Vila I.A.py
Exibindo Vila I.A.py. 
