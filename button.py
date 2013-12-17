#################################################################################
#                                                                               #
#                            button.py                                          #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem as definicoes da classe Button.                         #
#                                                                               #
#################################################################################


import pygame

from colors import *
from pygame.locals import *

class Button:

# Inicializa a classe
    #
    # @in window: janela na qual esta celula pertence
    # @in deffault_color: cor padrao de fundo
    # @in font_color: cor da fonte
    def __init__(self,window):
        self.window = window
        self.default_color = (100,100,100)
        self.font_color = (0,0,0)

    #retorna a cor que devera ser usada no fundo do botao1
    def hover_color_button1(self):
        mouse = pygame.mouse.get_pos()
        #mudar de cor quando o mouse estiver em cima
        if mouse[0] > 20 and mouse[0] < 320 and mouse[1] < 70 and mouse[1] > 20:
            return (255,255,255)
        else:
            return self.default_color

    #retorna a cor que devera ser usada no fundo do botao2
    def hover_color_button2(self):
        mouse = pygame.mouse.get_pos()
        #mudar de cor quando o mouse estiver em cima
        if mouse[0] > 480 and mouse[0] < 780 and mouse[1] < 70 and mouse[1] > 20:
            return (255,255,255)
        else:
            return self.default_color

    #pinta o botao com as cores recebidas
    def paint_button1(self):
        pygame.draw.rect(self.window, self.hover_color_button1(), [20,20,300,50])
        pygame.draw.rect(self.window, self.font_color, [20,20,300,50], 1)
        font = pygame.font.Font(None, 50)
        self.window.blit(font.render("Calcular", 1, self.font_color), [100,25,200,20])   
    
    def paint_button2(self):
        pygame.draw.rect(self.window,self.hover_color_button2(),[480,20,300,50])
        pygame.draw.rect(self.window,self.font_color,[480,20,300,50],1)
        font = pygame.font.Font(None, 50)
        self.window.blit(font.render("Limpar Malha", 1, self.font_color),[520,25,300,20])
        
