#################################################################################
#                                                                               #
#                            log.py                                             #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem as definicoes da classe Log.                            #
#                                                                               #
#################################################################################

from time import gmtime, strftime
import pygame
from pygame.locals import *
from colors import *

# Inicializa a classe
    #
    # @in window: janela na qual esta celula pertence
    # @in deffault_color: cor padrao de fundo
    # @in font_color: cor da fonte
    # @in text: texto do log

class Log:
    
    def __init__(self,window):
        self.window = window
        self.background_color = white
        self.font_color = black
        self.text = "Inicio"

    #pinta a janela do log com o texto do evento
    def paint_log(self):
        pygame.draw.rect(self.window, self.background_color, [330,20,140,50])
        pygame.draw.rect(self.window, self.font_color, [330,20,140,50], 1)
        font = pygame.font.Font(None, 17)
        self.window.blit(font.render(self.text, 1, self.font_color), [335,25,200,20])

    #escreve o log
    def write_log(self):
        with open('/log.txt','a') as file: #diretorio
            file.write( "[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "]" + ":::"  + self.text + "\n")
            file.close()
