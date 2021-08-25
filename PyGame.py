import pygame
from sys import exit

from pygame import surface

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.image.load('graphics/skyfinal.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0,0))

    pygame.display.update()
    clock.tick(60) #Setting the frame rate