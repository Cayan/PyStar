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
        self.log = Log(self.window, pygame.Rect(280, 20, 240, 50), pygame.Rect(290, 25, 200, 20))
        
        self.game = Game(self.window, self.log, self.width - self.margin_left - self.margin_right, self.height - self.margin_top - self.margin_bottom)
        self.buttons.append(Button(self.window, pygame.Rect(20, 20, 250, 50), pygame.Rect(70, 25, 200, 20), "Calcular", self.game.start))
        self.buttons.append(Button(self.window, pygame.Rect(530, 20, 250, 50), pygame.Rect(605, 25, 200, 20), "Limpar", self.game.clear))
        
        #escreve o log do inicio
        self.log.update("Inicio")
     
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
                if event.button == 1:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].rect.collidepoint(pos):
                            self.buttons[i].onClick() # chamamos a funcao associada ao botao
                            break                       

                # Ajusta a posicao e tenta obter a celula sobre este.
                cell = self.game.getCellByPosition([pos[0] - self.margin_left, pos[1] - self.margin_top])
                if cell: # Caso encontrada
                    if event.button == 1:
                        self.game.updateCell(cell) # Atualiza esta.
                    if event.button == 3:
                        self.game.text = "Cell: " + str(cell.id) + ". Cost G: " + str(cell.cost_g) + ". Cost H: " + str(cell.cost_h)
            elif event.type == KEYDOWN: # Caso seja uma tecla pressionada.
                if event.key == K_F1:
                    self.game.clear()
                    self.log.update("Carregando mapa 1")
                    self.game.getCellById(55).color = gray
                    self.game.getCellById(206).color = yellow
                elif event.key == K_F2:
                    self.game.clear()
                    self.log.update("Carregando mapa 2")
                    self.game.getCellById(108).color = gray
                    self.game.getCellById(112).color = yellow
                    
                    self.game.getCellById(90).color = black
                    self.game.getCellById(110).color = black
                    self.game.getCellById(130).color = black
                    pass
                elif event.key == K_F3:
                    self.game.clear()
                    self.log.update("Carregando mapa 3")
                    self.game.getCellById(221).color = gray
                    self.game.getCellById(20).color = yellow
                    
                    self.game.getCellById(201).color = black
                    self.game.getCellById(202).color = black
                    self.game.getCellById(224).color = black
                    self.game.getCellById(204).color = black
                    self.game.getCellById(184).color = black
                    self.game.getCellById(162).color = black
                    self.game.getCellById(142).color = black
                    self.game.getCellById(122).color = black
                    self.game.getCellById(123).color = black
                    self.game.getCellById(124).color = black
                    self.game.getCellById(125).color = black
                    self.game.getCellById(126).color = black
                    self.game.getCellById(127).color = black
                    self.game.getCellById(164).color = black
                    self.game.getCellById(225).color = black
                    self.game.getCellById(205).color = black
                    self.game.getCellById(185).color = black
                    self.game.getCellById(165).color = black
                    self.game.getCellById(81).color = black
                    self.game.getCellById(82).color = black
                    self.game.getCellById(83).color = black
                    self.game.getCellById(84).color = black
                    self.game.getCellById(85).color = black
                    self.game.getCellById(86).color = black
                    self.game.getCellById(87).color = black
                    self.game.getCellById(88).color = black
                    self.game.getCellById(89).color = black
                    self.game.getCellById(147).color = black
                    self.game.getCellById(167).color = black
                    self.game.getCellById(187).color = black
                    self.game.getCellById(207).color = black
                    self.game.getCellById(227).color = black
                    self.game.getCellById(109).color = black
                    self.game.getCellById(129).color = black
                    self.game.getCellById(149).color = black
                    self.game.getCellById(169).color = black
                    self.game.getCellById(189).color = black
                    self.game.getCellById(209).color = black
                    self.game.getCellById(231).color = black
                    self.game.getCellById(211).color = black
                    self.game.getCellById(191).color = black
                    self.game.getCellById(171).color = black
                    self.game.getCellById(151).color = black
                    self.game.getCellById(131).color = black
                    self.game.getCellById(111).color = black
                    self.game.getCellById(91).color = black
                    self.game.getCellById(71).color = black
                    self.game.getCellById(51).color = black
                    self.game.getCellById(50).color = black
                    self.game.getCellById(49).color = black
                    self.game.getCellById(48).color = black
                    self.game.getCellById(47).color = black
                    self.game.getCellById(46).color = black
                    self.game.getCellById(26).color = black
                    self.game.getCellById(44).color = black
                    self.game.getCellById(43).color = black
                    self.game.getCellById(42).color = black
                    self.game.getCellById(1).color = black
                    self.game.getCellById(2).color = black
                    self.game.getCellById(3).color = black
                    self.game.getCellById(4).color = black
                    self.game.getCellById(8).color = black
                    self.game.getCellById(30).color = black
                    self.game.getCellById(12).color = black
                    self.game.getCellById(13).color = black
                    self.game.getCellById(232).color = black
                    self.game.getCellById(212).color = black
                    self.game.getCellById(192).color = black
                    self.game.getCellById(172).color = black
                    self.game.getCellById(152).color = black
                    self.game.getCellById(132).color = black
                    self.game.getCellById(34).color = black
                    self.game.getCellById(55).color = black
                    self.game.getCellById(76).color = black
                    self.game.getCellById(97).color = black
                    self.game.getCellById(118).color = black
                    self.game.getCellById(139).color = black
                    self.game.getCellById(156).color = black
                    self.game.getCellById(135).color = black
                    self.game.getCellById(93).color = black
                    self.game.getCellById(72).color = black
                    self.game.getCellById(52).color = black
                    self.game.getCellById(73).color = black
                    self.game.getCellById(94).color = black
                    self.game.getCellById(136).color = black
                    self.game.getCellById(157).color = black
                    self.game.getCellById(159).color = black
                    self.game.getCellById(179).color = black
                    self.game.getCellById(199).color = black
                    self.game.getCellById(233).color = black
                    self.game.getCellById(134).color = black
                    self.game.getCellById(154).color = black
                    self.game.getCellById(174).color = black
                    self.game.getCellById(194).color = black
                    self.game.getCellById(195).color = black
                    self.game.getCellById(197).color = black
                    self.game.getCellById(198).color = black
                    self.game.getCellById(215).color = black
                    self.game.getCellById(216).color = black
                    self.game.getCellById(217).color = black
                    self.game.getCellById(218).color = black
                    self.game.getCellById(219).color = black
                    self.game.getCellById(14).color = black
                    self.game.getCellById(15).color = black
                    self.game.getCellById(35).color = black
                    self.game.getCellById(37).color = black
                    self.game.getCellById(38).color = black
                    self.game.getCellById(39).color = black
                    self.game.getCellById(40).color = black
                    self.game.getCellById(58).color = black
                    self.game.getCellById(60).color = black
                    self.game.getCellById(80).color = black
                    self.game.getCellById(100).color = black
        return True

    def onExit(self):
        #escreve o log do fim
        self.log.update("Fim")
