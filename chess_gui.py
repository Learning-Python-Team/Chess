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
    game = ChessGame(window, WIDTH, HEIGHT, CHECKERSIZE)
    
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
            clock.tick(FPS)
            #pos = pygame.mouse.get_pos()
            
            ##### TEMPORARY CLI #####
            print (game.board)
            move_valid = False  # makes the input loop run at least once
            move = None
            while not move_valid:
                pinput = input(f'{game.board.turn}: ').lower()  # .lower() to make everything lowercase
                
                if pinput in ['quit', 'exit']:
                    print(f'{game.board.turn} quit the game.')
                    return 0
                
                move = game.board.getMove(pinput)
                
                if move is not None:
                    move_valid = game.board.is_valid_move(move)
                if not move_valid:
                    print(f'Move [{pinput}] is not valid.')
                    
                logging.debug(f"Move valid? {move_valid}")
                
            game.board.move(move)
            ##### TEMPORARY CLI #####
            
            game.redrawWindow()
            
            pygame.display.update()

        pygame.display.update()
    
if __name__ == '__main_':
    main()
    
