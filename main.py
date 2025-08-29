Conversa aberta. 1 mensagem não lida.

Pular para o conteúdo
Como usar o E-mail de Uninove com leitores de tela
Esta versão não é mais compatível. Faça upgrade para um navegador aceito.

2 de 58
Versão 0.1 do Arcádia
Externa
Caixa de entrada

Guilherme M. <guilhermematos.ofc@gmail.com>
Anexos
16:43 (há 2 horas)
para Guilherme, mim


1 anexo
  •  Anexos verificados pelo Gmail
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
