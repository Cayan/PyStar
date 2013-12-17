
#################################################################################
#                                                                               #
#                                   Cell.py                                     #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem as definicoes da classe Cell.                           #
#                                                                               #
#################################################################################

import pygame

from colors import *
from pygame.locals import *

class Cell:
    color = blue
    border_thickness = 1
    border_color = green

    # Inicializa a classe
    #
    # @in window: janela na qual esta celula pertence
    # @in id: identificador da celula
    # @in rect: rect do objeto
    def __init__(self, window, id, rect):
        self.window = window
        self.id = id
        self.rect = rect
     
    # Pinta o objeto
    #
    # @in rect: rect da regiao para ser pintada
    def paint(self, rect):
        # Primeiro pintamos todo o objeto e depois pintamos por cima a borda deste.
        pygame.draw.rect(self.window, self.color, [self.rect.left + rect.left, self.rect.top + rect.top, self.rect.width, self.rect.height])
        pygame.draw.rect(self.window, self.border_color, [self.rect.left + rect.left, self.rect.top + rect.top, self.rect.width, self.rect.height], self.border_thickness)
