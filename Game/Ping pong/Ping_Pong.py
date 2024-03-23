# JP0030

import pygame
import sys
import random
import time

pygame.init()

c = pygame.time.Clock()

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Ping Pong Game")

ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30, )
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)

