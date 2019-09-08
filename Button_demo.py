import pygame
from src.pygame_classes import Button

pygame.init()
win =  pygame.display.set_mode((500, 500))
win.fill((255,255,255))

def redrawWindow():
    win.fill((255,255,255))
    toggleButton.draw(win, (0,0,0))
    normalButton.draw(win, (0,0,0))

run = True
toggleButton = Button(((0,255,0),(255,0,0)), 150, 105, 250, 100, text='Toggle Demo', toggle=True)
normalButton = Button(((0,255,0),(255,0,0)), 150, 255, 250, 100, text='Normal Demo')
while run:
    redrawWindow()
    pygame.display.update()
    
    pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        toggleButton.check(event, pos)
        normalButton.check(event, pos)
