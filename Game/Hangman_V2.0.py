# JP0030

import pygame
import sys
import random
import time

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Hangman")
icon = pygame.image.load("img_9.png")
pygame.display.set_icon(icon)

game_over = False

row = 2
col = 13
gap = 20
size = 40
boxes = []

for row in range(row):
    for col in range(col):
        x = ((col * gap) + gap) + (size * col)
        y = ((row * gap) + gap) + (size * row) + 330
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

        