import pygame

from pygame.locals import*

img = pygame.image.load('src/Sprites/h50bx/Chess_qlt45.svg.png')



white = (255, 255, 255)


screen = pygame.display.set_mode((800, 800))

screen.fill((white))

running = True




while running:

    screen.fill((white))

    screen.blit(img,(0,0))

    pygame.display.flip()
