#Blibiotecas
import pygame

#Configurações da Janela
largura_tela = 1280 #X - Coluna
altura_tela = 680 #Y - Largura
tamanho_da_celula = 20

#Configurações do Mapa
mapa_coluna = 200
mapa_linha = 200



#Cores
fundo = (30,30,30) 
cor_da_grade = (100,100,100)
cor_obstaculo = (180, 60, 60)
cor_debug = (200, 200, 50)

#Mapa
def criar_mapa(linhas,colunas):
    grid = [[ 0 for x in range(colunas)] for y in range(linhas)]

    #Futuras Criações de estruturas, reservar valores e alterar de zero para 1: Obstaculo
    
    return grid

#Visual    
def desenhar_mapa(tela, grid, cam_coluna, cam_linha):
    
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
                
                
                
        
#Execução do programa
def main():
    
    #Start e Parâmetros 
    pygame.init()
    pygame.display.set_caption("Path Neural")   #Nome Provisório
    
    tela = pygame.display.set_mode((largura_tela, altura_tela)) #Tamanho da Tela        
    
    grid = criar_mapa(mapa_linha, mapa_coluna)
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
                cam_coula = cam_coluna + 1
            if teclas[pygame.K_UP]:
                cam_linha = cam_linha - 1
            if teclas[pygame.K_DOWN]:
                cam_linha = cam_linha + 1
                
            #Fechando o Aplicativo
            if eventos.type == pygame.QUIT:
                loop = False


        desenhar_mapa(tela, grid, cam_coluna, cam_linha)
        pygame.display.flip() 

    pygame.quit()

#Iniciar Programa
main()

