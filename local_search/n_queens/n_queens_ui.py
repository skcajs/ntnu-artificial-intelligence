import pygame
from pygame.locals import *

from n_queens import create_board, successors, heuristic
from utils import Problem, Node
from hill_climbing import HillClimbing

import numpy as np

pygame.init()

n = 10
board = create_board(n)

problem = Problem(initial_state=board, f_heuristic=heuristic, f_successors=successors)
hc = HillClimbing(problem)

markers = hc.search()

screen_width = n*100
screen_height = n*100 + 100

# global variables
line_width = 6

# colors
blue = (0,0,255)

# fonts
font = pygame.font.SysFont(None, 80)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('N Queen Puzzle')

def draw_grid():
    screen.fill((255, 255, 200))
    grid = (50,50,50)
    for x in range(1,n):
        pygame.draw.line(surface=screen, color=grid, start_pos=(0, x*100), end_pos=(screen_width, x*100), width=line_width)
        pygame.draw.line(surface=screen, color=grid, start_pos=(x*100, 0), end_pos=(x*100, screen_height-100), width=line_width)
    pygame.draw.line(surface=screen, color=grid, start_pos=(0, screen_height-100), end_pos=(screen_width, screen_height-100), width=line_width)

def draw_markers(i):
    state = np.array(list(markers[i]))
    board = state[0]
    val = state[1]
    y = 0
    for row in board:
        x = 0
        for i in row:
            if i == 0.:
                x += 100
                continue
            num_img = font.render('X', True, blue, None) 
            screen.blit(num_img, (x+35, y+25))
            x += 100
        y += 100
    val_img = font.render(str(val), True, blue, None)
    screen.blit(val_img, (int(screen_width/2)-20, screen_height-75))

tic = pygame.time.get_ticks()

run = True
i = 0
while run:
    toc = pygame.time.get_ticks()
    draw_grid()
    draw_markers(i)
    
    if toc - tic >= 500:
        if (i == len(markers)-1):
            while True:
                run = False
        tic = toc
        i += 1


  
    # last function in game loop
    pygame.display.update()
