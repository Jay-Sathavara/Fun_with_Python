# JP003

import pygame
import requests

pygame.init()

width = 550
height = 550

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

font = pygame.font.Font("freesansbold.ttf", 35)


response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
s_grid = response.json()['board']
grid_original = [[s_grid[x][y] for y in range(len(s_grid[0]))] for x in range(len(s_grid))]
grid_color = (52, 31, 151)

def insert(screen, position):
    i, j = position[1], position[0]
    font = pygame.font.Font("freesansbold.ttf", 35)
    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                return
           if event.type == pygame.KEYDOWN:
                 if (grid_original[i - 1][j - 1] != 0):
                    return
                 if (event.key == 48):
                    s_grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (position[0] * 50 + 5, position[1] * 50 + 10, 50 - 10, 50 - 10))
                    pygame.display.update()
                 if (0 < event.key - 48 < 10): 
                         pygame.draw.rect(screen, (255, 255, 255),(position[0] * 50 + 5, position[1] * 50 + 10, 50 - 10, 50 - 10))
                         value = font.render(str(event.key - 48), True, (0, 0, 0))
                         screen.blit(value, (position[0] * 50 + 15, position[1] * 50))
                         s_grid[i - 1][j - 1] = event.key - 48
                         pygame.display.update()
    return

running = True
while running:
    screen.fill((255, 255, 255))
    # Checking the event
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            insert(screen, (pos // 50, pos // 50))
        if event.type == pygame.QUIT:
            running = False