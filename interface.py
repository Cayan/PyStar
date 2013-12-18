# -*- coding: utf-8 -*-
#################################################################################
#                                                                               #
#                                   Interface.py                                #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem as definicoes da classe Interface.                      #
#                                                                               #
#################################################################################

import os
import sys
import pygame

from game import *
from colors import *
from pygame.locals import *

class Interface:
    width = 800
    height = 600
    caption = ""
    margin_left = 20
    margin_right = 20
    margin_top = 100
    margin_bottom = 20
    background_color = white
    buttons = [] # inicializa o vetor de botoes

    # Inicializa a classe
    #
    # @in width: largura do tabuleiro
    # @in height: altura do tabuleiro
    # @in caption: titulo da janela
    def __init__(self, width, height, caption):
        self.height = height
        self.width = width
        self.caption = caption
        self.create()

    # Cria a janela e o objeto to tabuleiro.
    def create(self):
        pygame.init() # Inicializa os modulos do pygame
        pygame.display.set_caption(self.caption) # Ajusta o titulo
        self.window = pygame.display.set_mode((self.width, self.height), 0, 32) # Cria a janela
        self.log = Log(self.window, pygame.Rect(280, 20, 240, 50), pygame.Rect(335, 25, 200, 20))
        
        self.game = Game(self.window, self.log, self.width - self.margin_left - self.margin_right, self.height - self.margin_top - self.margin_bottom)
        self.buttons.append(Button(self.window, pygame.Rect(20, 20, 250, 50), pygame.Rect(70, 25, 200, 20), "Calcular", self.game.start))
        self.buttons.append(Button(self.window, pygame.Rect(530, 20, 250, 50), pygame.Rect(605, 25, 200, 20), "Limpar", self.clear))
        
        #escreve o log do inicio
        self.log.update("Inicio")
     
    # Reinicia o valor das celulas.
    def clear(self):
        self.log.update("Limpa a malha")
        for i in range(len(self.game.cells)):
            for j in range(len(self.game.cells[i])):
                self.game.cells[i][j].color = blue   

    # Limpa a janela, pinta o tabuleiro e seus objetos e depois atualiza a janela.
    def paint(self):
        self.window.fill(self.background_color)

        # Atualiza o tabuleiro
        self.game.paint(pygame.Rect(self.margin_left, self.margin_top, self.game.width, self.game.height))
        
        # Atualiza os botoes
        for i in range(len(self.buttons)):
            self.buttons[i].paint()
                    
        #Atualiza o log screen
        self.log.paint()

        pygame.display.update()
        
    # Funcao que roda o tempo todo para determinar os eventos.
    def update(self):
        # Pinta a janela.
        self.paint()
        
        # Atualiza o tabuleiro.
        self.game.update()
       
        # Verifica eventos.
        for event in pygame.event.get():
            if event.type == QUIT: # Caso haja uma notificacao para fechar.
                pygame.quit()
                return False
            elif event.type == MOUSEBUTTONUP: # Caso haja uma notificacao de clique.
                pos = pygame.mouse.get_pos() # Obtem onde foi efetuado o clique.

                # Verificamos se o clique foi sobre um botao
                for i in range(len(self.buttons)):
                    if self.buttons[i].rect.collidepoint(pos):
                        self.buttons[i].onClick() # chamamos a funcao associada ao botao
                        break                       

                # Ajusta a posicao e tenta obter a celula sobre este.
                cell = self.game.getCell([pos[0] - self.margin_left, pos[1] - self.margin_top])
                if cell: # Caso encontrada,atualiza o log.
                    self.game.updateCell(cell) # Atualiza esta.

        return True

    def onExit(self):
        #escreve o log do fim
		self.log.update("Fim")
