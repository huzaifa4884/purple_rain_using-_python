import pygame
import random
import sys
import time

from pygame import draw
from pygame.time import Clock

pygame.init()

blue = (230 , 230 , 250)
black = ( 0, 0,0)
white = (250 , 250 , 250)


gravity = 5

FPS = 60

width = 900
height = 600

snow_size = 8
gameOver = False

display = pygame.display.set_mode((width , height))
pygame.display.set_caption('Snow')

snow_flake = []

for i in range(1100):
    x = int(random.randrange(0,width))
    y = int(random.randrange(0 , height))
    z = random.randrange(7 , 10)
    snow_flake.append([x,y,z])

clock = pygame.time.Clock()
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            gameOver = True
    display.fill(blue, rect=None, special_flags=0)

    for i in snow_flake:
        i[1] += i[2]
        i[2] += 0.3
        len = random.randrange(10 , 20)

        pygame.draw.line(display, (138,43,226), [i[0] , i[1]], [i[0] ,i[1]+len], width=2)

        if (i[1] > height):
            i[1] = int(random.randrange(-50 , -5))
            i[0] = int(random.randrange(width))
            i[2] = random.randrange(4 , 10)

    pygame.display.flip()
    clock.tick(FPS) 