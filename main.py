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

    window_size = 200, 200
    length_of_unit_square = int(window_size[0] / 8)
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    
    font = pygame.font.SysFont('Arial', 20)
    
    board = Board()

    colors = {
        'White': (255, 255, 255),
        'Black': (0, 0, 0)
        }

    print(board)
    for row in Board().game_board:
        for square in row:
            if square.row % 2 == 0:
                if square.column % 2 == 0:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(square.row * length_of_unit_square,
                                                                          square.column * length_of_unit_square,
                                                                          length_of_unit_square, length_of_unit_square))
                else:
                    pass
            else:
                if square.column % 2 == 1:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(square.row * length_of_unit_square,
                                                                          square.column * length_of_unit_square,
                                                                          length_of_unit_square, length_of_unit_square))
                else:
                    pass
    
    pygame.display.flip()
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
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(square.row, square.column, 10, 10))
                # print(square.row, square.column, square.piece)
        pygame.display.flip()
        board.move(move)


# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
