from chess_pieces import *
from board import *
import logging

logging.getLogger().setLevel(logging.DEBUG)

#main_logger = logging.getLogger('main')
#main_logger.setLevel(logging.DEBUG)

def main():
    '''
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    '''
    board = Board()
    
    while True:
        print (board)
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
            
        board.move(move)
               
# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
