import pygame
from sys import exit
from pygame import surface

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf',50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('My game', False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect =snail_surf.get_rect(bottomright =(600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (70, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(300, 50))
    screen.blit(snail_surf,snail_rect)
    snail_rect.x -=2.5
    if snail_rect.right <= 0: snail_rect.left = 800
    player_rect.left += 1
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(snail_rect):
        print('collision')

    pygame.display.update()
    clock.tick(60) #Setting the frame rate