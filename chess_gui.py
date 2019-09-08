from src.pygame_classes import *
import pygame
from pygame.locals import *

WIDTH = 460
HEIGHT = 460
FPS = 60
CHECKERSIZE = (60,60)
        
                
def main():
    pygame.init()
    window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption('Chess -- by the r/learningpython team')
    clock = pygame.time.Clock()
    
    startButton = Button(((200,200,200),(80,80,80)), 190, 210, 80, 40, text='Start')
    
    menu_runs = True
    game_runs = False
    while menu_runs:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        window.fill((50,50,50))
        startButton.draw(window)
        
        for event in pygame.event.get():
            if startButton.check(event, pos):
                game_runs = True
                
        while game_runs:
            game = ChessGame(window, WIDTH, HEIGHT, CHECKERSIZE)
            clock.tick(FPS)
            #pos = pygame.mouse.get_pos()
            
            game.redrawWindow()
            
            pygame.display.update()

        pygame.display.update()
    
if __name__ == '__main_':
    main()
    
