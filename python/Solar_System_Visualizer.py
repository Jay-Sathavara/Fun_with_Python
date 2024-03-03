# JP0030

import pygame
import math
import os

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("JP0030 - Solar System Visualizer")

sun_image = pygame.image.load(os.path.join("planets", "sun.png"))
mercury_image = pygame.image.load(os.path.join("planets", "mercury.png"))
venus_image = pygame.image.load(os.path.join("planets", "venus.png"))
earth_image = pygame.image.load(os.path.join("planets", "earth.png"))
mars_image = pygame.image.load(os.path.join("planets", "mars.png"))
jupiter_image = pygame.image.load(os.path.join("planets", "jupiter.png"))
saturn_image = pygame.image.load(os.path.join("planets", "saturn_ring.png"))
uranus_image = pygame.image.load(os.path.join("planets", "uranus.png"))
neptune_image = pygame.image.load(os.path.join("planets", "neptune.png"))

background_image = pygame.image.load(os.path.join("planets", "space.png"))

sun_image = pygame.transform.scale(sun_image, (80, 80))
mercury_image = pygame.transform.scale(mercury_image, (15, 15))
venus_image = pygame.transform.scale(venus_image, (25, 25))
earth_image = pygame.transform.scale(earth_image, (30, 30))
mars_image = pygame.transform.scale(mars_image, (20, 20))
saturn_image = pygame.transform.scale(saturn_image, (100, 40))
uranus_image = pygame.transform.scale(uranus_image, (35, 35))
jupiter_image = pygame.transform.scale(jupiter_image, (50, 50))
neptune_image = pygame.transform.scale(neptune_image, (40, 40))

