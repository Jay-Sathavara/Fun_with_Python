# JP0030

import pygame
import math
import os

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("JP0030 - Solar System Visualizer")

sun_image = pygame.image.load(os.path.join("planets", "Sun.png"))
mercury_image = pygame.image.load(os.path.join("planets", "Mercury.png"))
venus_image = pygame.image.load(os.path.join("planets", "Venus.png"))
earth_image = pygame.image.load(os.path.join("planets", "Earth.png"))
mars_image = pygame.image.load(os.path.join("planets", "Mars.png"))
jupiter_image = pygame.image.load(os.path.join("planets", "Jupiter.png"))
saturn_image = pygame.image.load(os.path.join("planets", "Saturn.png"))
uranus_image = pygame.image.load(os.path.join("planets", "Uranus.png"))
neptune_image = pygame.image.load(os.path.join("planets", "Neptune.png"))

background_image = pygame.image.load(os.path.join("planets", "Space.jpg"))

sun_image = pygame.transform.scale(sun_image, (80, 80))
mercury_image = pygame.transform.scale(mercury_image, (15, 15))
venus_image = pygame.transform.scale(venus_image, (25, 25))
earth_image = pygame.transform.scale(earth_image, (30, 30))
mars_image = pygame.transform.scale(mars_image, (20, 20))
saturn_image = pygame.transform.scale(saturn_image, (100, 40))
uranus_image = pygame.transform.scale(uranus_image, (35, 35))
jupiter_image = pygame.transform.scale(jupiter_image, (50, 50))
neptune_image = pygame.transform.scale(neptune_image, (40, 40))

planets = [
    {"name": "Sun", "image": sun_image, "radius": 200, "x": 400, "y": 390, "vx": 0, "vy": 0},
    {"name": "Mercury", "image": mercury_image, "angle": 0, "distance": 65, "period": 0.24, "radius": 10},
    {"name": "Venus", "image": venus_image, "angle": 0, "distance": 90, "period": 0.62, "radius": 20},
    {"name": "Earth", "image": earth_image, "angle": 0, "distance": 125, "period": 1, "radius": 25},
    {"name": "Mars", "image": mars_image, "angle": 0, "distance": 155, "period": 1.88, "radius": 15},
    {"name": "Jupiter", "image": jupiter_image, "angle": 0, "distance": 195, "period": 11.86, "radius": 45},
    {"name": "Saturn", "image": saturn_image, "angle": 0, "distance": 260, "period": 29.5, "radius": 40},
    {"name": "Uranus", "image": uranus_image, "angle": 0, "distance": 320, "period": 84, "radius": 30},
    {"name": "Neptune", "image": neptune_image, "angle": 0, "distance": 370, "period": 164.8, "radius": 35}
]

for planet in planets[1:]:
    planet["x"] = planets[0]["x"] + math.cos(planet["angle"]) * planet["distance"]
    planet["y"] = planets[0]["y"] + math.sin(planet["angle"]) * planet["distance"]

for planet in planets[1:]:
    planet["past_positions"] = []

clock = pygame.time.Clock()
fps = 30

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    image_rect = planets[0]["image"].get_rect()
    image_rect.center = (int(planets[0]["x"]), int(planets[0]["y"]))
    screen.blit(planets[0]["image"], image_rect)
   
    for planet in planets[1:]:
        planet["angle"] += 0.05 * (1 / planet["period"])

        planet["x"] = planets[0]["x"] + math.cos(planet["angle"]) * planet["distance"]
        planet["y"] = planets[0]["y"] + math.sin(planet["angle"]) * planet["distance"]

        planet["past_positions"].append((planet["x"], planet["y"]))

        for i in range(1, len(planet["past_positions"])):
            pygame.draw.line(screen, (153,153,0), planet["past_positions"][i-1], planet["past_positions"][i], 1)

        image_rect = planet["image"].get_rect()
        image_rect.center = (int(planet["x"]), int(planet["y"]))
        
        screen.blit(planet["image"], image_rect)

    pygame.display.update()

    clock.tick(fps)

pygame.quit()