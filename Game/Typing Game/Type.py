# JP0030

import pygame
import random
import time

pygame.init()
WIDTH = 800
HEIGHT = 600
whit=(0,0,0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JP0030 -  Keyboard Jump Game')
background = pygame.image.load('keyback.jpeg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  
font = pygame.font.Font('comic.ttf', 40)