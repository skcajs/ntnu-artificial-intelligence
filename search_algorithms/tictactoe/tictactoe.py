import math
import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

# global variables
line_width = 6
markers = []
pos = []
clicked = False
player = 1
winner = 0
game_over = False
draw = False

# colors
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

# fonts
font = pygame.font.SysFont(None, 40)

# play again rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

def draw_grid():
    screen.fill((255, 255, 200))
    grid = (50,50,50)
    for x in range(1,3):
        pygame.draw.line(surface=screen, color=grid, start_pos=(0, x*100), end_pos=(screen_width, x*100), width=line_width)
        pygame.draw.line(surface=screen, color=grid, start_pos=(x*100, 0), end_pos=(x*100, screen_height), width=line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(surface=screen, color=green, start_pos=( x_pos * 100 + 15, y_pos * 100 + 15), end_pos=(x_pos * 100 + 85, y_pos * 100 + 85), width=line_width)
                pygame.draw.line(surface=screen, color=green, start_pos=( x_pos * 100 + 15, y_pos * 100 + 85), end_pos=(x_pos * 100 + 85, y_pos * 100 + 15), width=line_width)
            if y == -1:
                pygame.draw.circle(surface=screen, color=red, center=(x_pos * 100 + 50, y_pos * 100 + 50), radius=38, width=line_width)
            y_pos += 1
        x_pos += 1


for x in range(3):
    row = [0] * 3
    markers.append(row)


def check_winner():

    global winner
    global draw
    global game_over

    y_pos = 0
    for x in markers:
        # check columns
        if sum(x) == 3:
            winner = 'X'
            game_over = True
        if sum(x) == -3:
            winner = 'O'
            game_over = True
        # check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 'X'
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 'O'
            game_over = True
        y_pos += 1

    # check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 'X'
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 'O'
        game_over = True

    if not any(0 in submarkers for submarkers in markers) and winner == 0:
        winner = 'D'
        draw = True
        game_over = True

def test_winner():
    y_pos = 0
    for x in markers:
        # check columns
        if sum(x) == 3:
            return 'X'

        if sum(x) == -3:
            return 'O'

        # check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            return 'X'

        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            return 'O'

        y_pos += 1

    # check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        return 'X'

    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        return 'O'

    if not any(0 in submarkers for submarkers in markers) and winner == 0:
        return 'D'


def draw_winner(winner):
    win_text = "Player " + winner + " wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = "Play Again?"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))

def draw_draw():
    draw_text = "Draw!"
    draw_img = font.render(draw_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(draw_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = "Play Again?"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))

def AI_move():
    bestScore = - math.inf
    bestMove = 0,0
    for i in range(len(markers)):
        for j in range(len(markers[i])):
            if markers[i][j] == 0:
                markers[i][j] = -1
                score = minimax(markers, False)
                markers[i][j] = 0
                if score > bestScore:
                    bestScore = score
                    bestMove = i,j
    return bestMove

def minimax(markers, isMaximising):
    test_win = test_winner()
    if test_win == 'O':
        return 1
    elif test_win == 'X':
        return -1
    elif test_win == 'D':
        return 0
    
    if isMaximising:
        bestScore = - math.inf
        for i in range(len(markers)):
            for j in range(len(markers[i])):
                if markers[i][j] == 0:
                    markers[i][j] = -1
                    score = minimax(markers, False)
                    markers[i][j] = 0
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = math.inf
        for i in range(len(markers)):
            for j in range(len(markers[i])):
                if markers[i][j] == 0:
                    markers[i][j] = 1
                    score = minimax(markers, True)
                    markers[i][j] = 0
                    if score < bestScore:
                        bestScore = score
        return bestScore



run = True
while run:
    
    draw_grid()
    draw_markers()

    #  event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over:
            if player == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                    clicked = False
                    pos = pygame.mouse.get_pos()
                    cell_x = pos[0]
                    cell_y = pos[1]
                    if markers[cell_x // 100][cell_y // 100] == 0:
                        markers[cell_x // 100][cell_y // 100] = player
                        player *= -1
                        check_winner()
            else:
                ai_x, ai_y = AI_move()
                markers[ai_x][ai_y] = player
                player *= -1
                check_winner()

    if game_over:
        if (draw):
            draw_draw()
        else:
            draw_winner(winner)
        # check for mouseclick to see if user has chosen play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                markers = []
                pos = []
                player = 1
                winner = 0
                draw = False
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    markers.append(row)


    # last function in game loop
    pygame.display.update()

pygame.quit()