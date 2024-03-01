# JP0030

import pygame, sys
import os
import random

player_lives = 3                                                #keep track of lives
score = 0                                                       #keeps track of score
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']    #entities in the game

# initialize pygame and create window
WIDTH = 800
HEIGHT = 500
FPS = 12                                                 #controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
pygame.init()
pygame.display.set_caption('Fruit-Ninja Game -- DataFlair')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   #setting game display size
clock = pygame.time.Clock()

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)