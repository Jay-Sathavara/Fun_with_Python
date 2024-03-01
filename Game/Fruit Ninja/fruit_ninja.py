# JP0030

import pygame, sys
import os
import random

player_lives = 3
score = 0     
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']    


WIDTH = 800
HEIGHT = 500
FPS = 12   
pygame.init()
pygame.display.set_caption('Fruit-Ninja Game -- DataFlair')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   
clock = pygame.time.Clock()


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

background = pygame.image.load('back.jpg') 
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255)) 
lives_icon = pygame.image.load('images/white_lives.png')           

def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x' : random.randint(100,500),          
        'y' : 800,
        'speed_x': random.randint(-10,10),      
        'speed_y': random.randint(-80, -60),  
        'throw': False,                        
        't': 0,                                
        'hit': False,
    }

    if random.random() >= 0.75:    
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))

