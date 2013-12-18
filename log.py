#################################################################################
#                                                                               #
#                            log.py                                             #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem as definicoes da classe Log.                            #
#                                                                               #
#################################################################################

import pygame

from time import gmtime, strftime
from pygame.locals import *
from colors import *

class Log:
    background_color = white
    font_color = black
    border_color = black
    border_thickness = 1
    
    # Inicializa a classe
    #
    # @in window: janela principal
    # @in rect: rect do objeto
    # @in font_rect: rect do texto
    def __init__(self, window, rect, font_rect):
        self.window = window
        self.rect = rect
        self.font_rect = font_rect
        
        self.font = pygame.font.Font(None, 17)
        
    # Pinta a janela do log com o texto do evento
    def paint(self):
        pygame.draw.rect(self.window, self.background_color, self.rect)
        pygame.draw.rect(self.window, self.border_color, self.rect, self.border_thickness)
        
        self.window.blit(self.font.render(self.text, 1, self.font_color), self.font_rect)

    # Atualiza as mensagens de log.
	#
	# @in text: texto a ser inserido.
    def update(self, text):
        self.text = text
        with open('/log.txt','a') as file:
            file.write( "[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "]" + ":::"  + text + "\n")
            file.close()
