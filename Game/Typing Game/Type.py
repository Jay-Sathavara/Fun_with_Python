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

word_speed = 0.5
score = 0
def new_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300,700)     
    y_cor = 200  
    word_speed += 0.10
    yourword = ''
    words = open("words.txt").read().split(', ')
    displayword = random.choice(words)
new_word()