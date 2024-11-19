import pygame
import random
import numpy as np
from sys import exit

pygame.init()
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
dt = 0
GRID_SIZE = 50
speed = 2
tst = pygame.Surface((100,200))
tst.fill('Red')


player_pos = pygame.Vector2(325,225)


light_Green = 'chartreuse2'
dark_green = 'chartreuse3'
directions = {
    "up": pygame.Vector2(0, -1),
    "down": pygame.Vector2(0, 1),
    "left": pygame.Vector2(-1, 0),
    "right": pygame.Vector2(1, 0),
}
current_direction = random.choice(list(directions.values()))


def draw_grid():
    for x in range(0, width, GRID_SIZE):
        for y in range(0, height, GRID_SIZE):
            if (x // GRID_SIZE + y // GRID_SIZE) % 2 == 0:
                color = light_Green
            else:
                color = dark_green
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, color, rect)



def handle_movement():
    global current_direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        current_direction = directions['up']
        return current_direction
    elif keys[pygame.K_s]:
        current_direction = directions['down']
        return current_direction
    elif keys[pygame.K_a]:
        current_direction = directions['left']
        return current_direction
    elif keys[pygame.K_d]:
        current_direction = directions['right']
        return current_direction





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('Black')
    handle_movement()
    player_pos += current_direction * speed

    draw_grid()
    pygame.draw.circle(screen, "Blue", player_pos, 20)
    


    #screen.blit(tst, (350,175))

    pygame.display.flip()
    pygame.display.update()
    dt = clock.tick(60) / 1000