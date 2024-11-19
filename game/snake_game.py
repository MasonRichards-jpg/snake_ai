import pygame
import random
import numpy as np
from sys import exit

pygame.init()
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()




while True():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)