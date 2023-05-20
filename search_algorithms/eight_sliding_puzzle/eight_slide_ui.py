import pygame
from pygame.locals import *
from eight_slide import play
import numpy as np

pygame.init()

screen_width = 300
screen_height = 300

# global variables
line_width = 6
markers = play()
markers

# colors
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

# fonts
font = pygame.font.SysFont(None, 80)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('8 Slide Puzzle')

def draw_grid():
    screen.fill((255, 255, 200))
    grid = (50,50,50)
    for x in range(1,3):
        pygame.draw.line(surface=screen, color=grid, start_pos=(0, x*100), end_pos=(screen_width, x*100), width=line_width)
        pygame.draw.line(surface=screen, color=grid, start_pos=(x*100, 0), end_pos=(x*100, screen_height), width=line_width)

def draw_markers(i):
    state = np.array(list(markers[i]))
    turn = state.reshape(3,3)
    y = 0
    for row in turn:
        x = 0
        for i in row:
            if i == '0':
                x += 100
                continue
            num_img = font.render(i, True, blue, None) 
            screen.blit(num_img, (x+35, y+25))
            x += 100
        y += 100

tic = pygame.time.get_ticks()

run = True
i = len(markers)-1
while run:
    toc = pygame.time.get_ticks()
    draw_grid()
    draw_markers(i)
    
    if toc - tic > 500:
        if (i == 0):
            run = False
        tic = toc
        i -= 1


  
    # last function in game loop
    pygame.display.update()
