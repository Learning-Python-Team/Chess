from chess_pieces import *
from board import *
import logging
import pygame
import sys

# logging.getLogger().setLevel(logging.DEBUG)

# main_logger = logging.getLogger('main')
# main_logger.setLevel(logging.DEBUG)


def main():
    '''
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move_input on it if it is valid.
    It terminates once the game is won or a player quits the game.
    '''
    
    window_size = 100, 100
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    
    font = pygame.font.SysFont('Arial', 20)
    
    board = Board()

    print(board)
    for row in Board().game_board:
        for square in row:
            print(square.row, square.column, square.piece)
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(square.row, square.column, 10, 10))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        
        
        move_valid = False  # makes the input loop run at least once
        move = None
        while not move_valid:
            pinput = input(f'{board.turn}: ').lower()  # .lower() to make everything lowercase
            
            if pinput in ['quit', 'exit']:
                print(f'{board.turn} quit the game.')
                return 0
              
            move = board.getMove(pinput)
            
            if move is not None:
                move_valid = board.is_valid_move(move)
            if not move_valid:
                print(f'Move [{pinput}] is not valid.')
                
            logging.debug(f"Move valid? {move_valid}")

        print(board)
        for row in Board().game_board:
            for square in row:
                print(square.row, square.column, square.piece)
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(square.row, square.column, 10, 10))
        board.move(move)
        
        
# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
