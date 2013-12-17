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
    background_color_hovered = white
    background_color = gray
    font_color = black
    border_color = black
    border_thickness = 1

    # Inicializa a classe
    #
    # @in window: janela na qual este botao pertence
    def __init__(self, window, rect, font_rect,text, callback):
        self.window = window
        self.rect = rect
        self.font_rect = font_rect
        self.text = text
        self.callback = callback
        
        self.font = pygame.font.Font(None, 50)

    # Define qual é a cor de fundo com base na posicao do mouse.
    #
    # @in pos: posicao do mouse
    # @out: A cor de fundo.
    def getBackgroundColor(self, pos):
        if self.rect.collidepoint(pos):
            return self.background_color_hovered
        else:
            return self.background_color

    # Pinta o botao
    def paint(self):
        pos = pygame.mouse.get_pos() # Obtem a posicao do mouse.
        pos = [pos[0], pos[1]]
        
        pygame.draw.rect(self.window, self.getBackgroundColor(pos), self.rect)
        pygame.draw.rect(self.window, self.border_color, self.rect, self.border_thickness)
        
        self.window.blit(self.font.render(self.text, 1, self.font_color), self.font_rect)   
