
#################################################################################
#                                                                               #
#                                   Game.py                                     #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem as definicoes da classe Game.                           #
#                                                                               #
#################################################################################

import random
import pygame
import time

from cell import *
from colors import *
from button import *
from log import *

class Game:
    border_color = black
    border_thickness = 5
    color = gray
    cell_margin = 5
    cell_count_horizontal = 20
    cell_count_vertical = 12
    cell_width = 30
    cell_height = 30
    delay = 50
    pos_x = 5
    pos_y = 5

    # Inicializa a classe
    #
    # @in window: janela na qual esta celula pertence
    # @in width: largura do tabuleiro
    # @in height: altura do tabuleiro
    def __init__(self, window, width, height):
        self.window = window
        self.height = height
        self.width = width
        self.cells = [] # inicializa a matriz de celulas
        self.last = 0 # momento em que a ultima atualizacao de "posicao" foi feita.
        self.text = "" # texto que vai fazer um overlay em toda a tela
        random.seed() # inicializa a semente dos numeros pseudo-randomicos com o tempo atual.
        self.create()
        

    # Cria todas as celulas e as organiza na matriz.
    def create(self):
        left = 0
        top = 0
        id = 1
        for i in range(self.cell_count_vertical):
            row = []
            self.cells.append(row)
            for j in range(self.cell_count_horizontal):
                cell = Cell(self.window, id, pygame.Rect(left, top, self.cell_width, self.cell_height))

                left += self.cell_width + self.cell_margin
                row.append(cell)
                id += 1
                
            top += self.cell_height + self.cell_margin
            left = 0

    # Ajusta a ponto para o local onde as celulas comecam a ser pintadas e verifica se o ponto esta sobre alguma celula
    #
    # #in pos: vetor com a coordenada x e y, ajustada para o posicionamento local do tabuleiro.
    # @out: A celula sobre o ponto ou None.
    def getCell(self, pos):
        pos[0] -= self.border_thickness + (self.width - ((self.cell_width + self.cell_margin) * self.cell_count_horizontal))/2
        pos[1] -= self.border_thickness + (self.height - ((self.cell_height + self.cell_margin) * self.cell_count_vertical))/2
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j].rect.collidepoint(pos):
                    return self.cells[i][j]

        return None

    # Pinta o tabuleiro e suas celulas
    #
    # @in rect: rect da regiao para ser pintada, com as coordenadas left e top ajustadas para o posicionamento local do tabuleiro.
    def paint(self, rect):
        # Primeiro pintamos todo o tabuleiro e depois pintamos por cima a borda deste.
        pygame.draw.rect(self.window, self.color, rect)
        pygame.draw.rect(self.window, self.border_color, rect, self.border_thickness)

        # Ajustamos as coordenadas left e top para o ponto onde as celulas comecam a ser pintadas
        rect.left += self.border_thickness + (self.width - ((self.cell_width + self.cell_margin) * self.cell_count_horizontal))/2
        rect.top += self.border_thickness + (self.height - ((self.cell_height + self.cell_margin) * self.cell_count_vertical))/2
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.cells[i][j].paint(rect)
                
        # Pintamos o texto overlay
        font = pygame.font.Font(None, 80)
        text = font.render(self.text, True, red)
        self.window.blit(text, [self.width/2 - 120, self.height/2])


    # Atualizamos a cor da celula.
    #
    # @in cell: celula para ser alterada
    def updateCell(self, cell):
        if cell.color == blue:
            cell.color = gray
        elif cell.color == gray:
            cell.color = yellow
        elif cell.color == yellow:
            cell.color = blue
    
    # Funcao que roda o tempo todo para determinar os eventos.
    def update(self):
        # verifica se esta nas bordas e/ou preso.
        if ((self.cells[self.pos_y - 1][self.pos_x + 0].color != blue or self.pos_y == 0) and 
            (self.cells[self.pos_y + 0][self.pos_x - 1].color != blue or self.pos_x == 0) and 
            (self.pos_x + 1 == self.cell_count_horizontal or self.cells[self.pos_y + 0][self.pos_x + 1].color != blue) and 
            (self.pos_y + 1 == self.cell_count_vertical or self.cells[self.pos_y + 1][self.pos_x + 0].color != blue)):
            return
    
        millis = int(round(time.time() * 1000)) # Obtem o tempo em milisegundos.
        if millis - self.last > self.delay: # Verifica quanto tempo se passou desde a ultima atualizacao.
            rand_x = 0
            rand_y = 0
            if random.randint(0, 1) == 0: # Sorteia se o movimento vai ser em x ou em y
                rand_x = random.randint(0, 1)*2 - 1
            else:
                rand_y = random.randint(0, 1)*2 - 1
            
            if not (self.pos_x + rand_x >= 0 and self.pos_x + rand_x < self.cell_count_horizontal): # Verifica as bordas.
                rand_x = 0
            
            if not (self.pos_y + rand_y >= 0 and self.pos_y + rand_y < self.cell_count_vertical):  # Verifica as bordas.
                rand_y = 0
 
            if self.cells[self.pos_y + rand_y][self.pos_x + rand_x].color == blue:  # Verifica se esta na cor original.
                # Atualiza a celula atual.
                self.pos_x += rand_x
                self.pos_y += rand_y
                
                # Altera a cor da celula atual.
                self.updateCell(self.cells[self.pos_y][self.pos_x])
                
                # Determina que houve uma atualizacao, assim tera um intervalo ate a proxima.
                self.last = millis
