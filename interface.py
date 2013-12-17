
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
        self.btn = Button(self.window)
        self.log = Log(self.window)

    # Cria a janela e o objeto to tabuleiro.
    def create(self):
        pygame.init() # Inicializa os modulos do pygame
        pygame.display.set_caption(self.caption) # Ajusta o titulo
        self.window = pygame.display.set_mode((self.width, self.height), 0, 32) # Cria a janela
        
        self.game = Game(self.window, self.width - self.margin_left - self.margin_right, self.height - self.margin_top - self.margin_bottom)

    # Limpa a janela, pinta o tabuleiro e seus objetos e depois atualiza a janela.
    def paint(self):
        self.window.fill(self.background_color)

        self.game.paint(pygame.Rect(self.margin_left, self.margin_top, self.game.width, self.game.height))
        
        #Atualiza os botoes
        self.btn.paint_button1()
        self.btn.paint_button2()

        #Atualiza o log screen
        self.log.paint_log()

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

                #Verificamos se o clique foi na posicao do botao      
                #Funcao do botao 1, usar A*          
                if pos[0] > 20 and pos[0] < 320 and pos[1] < 70 and pos[1] > 20:
                    self.log.text = "Calcula caminho" #atualiza o log
                    self.log.write_log()

                #Funcao do botao 2,limpar a malha
                elif pos[0] > 480 and pos[0] < 780 and pos[1] < 70 and pos[1] > 20:
                    self.log.text = "Limpa a malha" #atualiza o log
                    self.log.write_log()
                    for i in range(len(self.game.cells)):
                        for j in range(len(self.game.cells[i])):
                                self.game.cells[i][j].color = blue      


                    #self.game.cells[i][j].paint(rect)                     

                # Ajusta a posicao e tenta obter a celula sobre este.
                cell = self.game.getCell([pos[0] - self.margin_left, pos[1] - self.margin_top])
                if cell: # Caso encontrada,atualiza o log.
                    if cell.color == blue:
                        self.log.text = "Atualiza " + str(cell.id) + " Blue -> Gray"
                        self.log.write_log()
                    if cell.color == gray:
                        self.log.text = "Atualiza " + str(cell.id) + " Gray -> Yellow"
                        self.log.write_log()
                    if cell.color == yellow:
                        self.log.text = "Atualiza " + str(cell.id) + " Yellow -> Blue"
                        self.log.write_log() 
                    self.game.updateCell(cell) # Atualiza esta.

        return True
