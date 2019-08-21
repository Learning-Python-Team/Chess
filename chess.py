from chess_pieces import *
import re
import logging 

logging.getLogger().setLevel(logging.DEBUG)

WHITE = "White"
BLACK = "Black"

def mirror(board): 
    logging.debug ("Flipping the board")
    # Make sure we don't change the actual board
    board = board.copy()

    # First flatten the list
    flat = []
    for row in board:
        flat.extend(row)
    board = reversed (flat)

    # Now pack the list into an 8x8
    result = []
    buffer_row = []
    for index, cell in enumerate(board, 1): 
        buffer_row.append(cell)
        # Clear buffer every 8th square
        if not index % 8:
            result.append (buffer_row)
            buffer_row = []


    return result

class Square:
    '''
    The Dataclass game_board is 'made' of
    '''
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.piece = NonePiece()

    def __str__(self): return str (self.piece)
    def __repr__(self): return str (self)

class Board:
    '''
    The Board class contains a list of square objects, as well as the function to initially set the game_board up,
    the function to check moves for vaildity,
    and the function for moving the pieces on board.
    '''
    def __init__(self):
        self.game_board = []

        for row in range(8):
            self.game_board.append([])
            for column in range(8):
                self.game_board[row].append(Square(row, column))  # generates a 2-dimensional list of square objects

        self.turn = WHITE
        self.setup()  # populates the board with the initial setup of pieces

    # These methods will help with getting and setting the pieces
    def __getitem__(self, tup): return self.game_board[tup [0]][tup [1]]
    def __setitem__(self, tup, value): 
        self.game_board[tup [0]] [tup [1]] = value
                
    def __str__(self):
        # Make sure you are using a monospace font
        result = ""
        board = self.game_board
        indices = range (8, 0, -1)
        if self.turn == BLACK:
            board = mirror(board)
            indices = range (1, 9)

        for row, index in zip (board, indices):
            result += "  |\n"
            result += f"{index} |  {('    ').join (map (str, row))}\n"

        result += "--+-------------------------------------------\n"
        if self.turn == WHITE:
            result += "  |  a    b    c    d    e    f    g    h\n"
        else: 
            result += "  |  h    g    f    e    d    c    b    a\n"


        return result

    def setup(self):
        logging.debug ("Setting up board")
        for row in self.game_board:
            for square in row:
                if square.row == 1: square.piece = Pawn(WHITE)
                elif square.row == 6: square.piece = Pawn(BLACK)
                elif square.row in (0, 7): 
                    color = BLACK if square.row == 7 else WHITE
                    if square.column in (0, 7): square.piece = Rook(color)
                    if square.column in (1, 6): square.piece = Knight(color)
                    if square.column in (2, 5): square.piece = Bishop(color)
                    if square.column == 3: square.piece = Queen(color)
                    if square.column == 4: square.piece = King(color)

    def move(self, move):
        """
        Moves the pieces from one square to another.
        Requires move to be of form: ( 
            (origin_row, origin_col), 
            (destination_row, destination_col)
        )
        """
        origin, destination = move
        logging.info(f"Moving piece from {origin} to {destination}")

        origin_square = self [origin]
        destination_square = self [destination]
        self [origin].piece.moved = True
        self [destination].piece = self [origin].piece
        self [origin].piece = NonePiece()

        # changing the player whose turn it is
        if self.turn == WHITE: self.turn = BLACK
        else: self.turn = WHITE
        logging.info(f"Switching turn to {self.turn}")

    def move_valid(self, move):
        """
        Tests whether or not the move specified is a valid move
        """
        return True  # DEBUG VALUE

    def getMove(self, move: str) -> ( (int, int), (int, int) ):
        """
        Parses move from str input.
        Move must be of form: 
            (origin_letter)(origin_number) + 
            (destination_letter)(destination_number)
        returns move of form: 
            ( (origin_row, origin_col), (destination_row, destination_col) )
        """

        # Maps a: 0, b: 1, etc.
        letter_to_index = {
            letter: index
            for letter, index in zip("abcdefgh", range (8))
        }

        # Rows are printed bottom to top but interpreted top to bottom
        # This maps 0-7 -> 7-0 to counter that. 
        rows = list (range (7, -1, -1))

        # Get moves from input
        matches = re.search(r'([abcdefgh][12345678])\s([abcdefgh][12345678])', move)
        if matches is None: return None  # cannot determine move
        origin = matches.group(1)  # origin
        origin = (
            rows [int(origin[1]) - 1],  # get the row
            letter_to_index[origin[0]]  # get the column
        )
        
        destination = matches.group(2)
        destination = (
            rows [int(destination[1]) - 1], 
            letter_to_index[destination[0]]
        ) 

        logging.debug(f"Move {move} interpreted as {(origin, destination)}")
        return origin, destination 

def main():
    '''
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    '''
    # players = Players(WHITE, BLACK)
    board = Board()
    
    while True:
        print (board)
        move_valid = False  # makes the input loop run at least 
        move = None
        while not move_valid:
            pinput = input(f'{board.turn}: ').lower()  # .lower() to make everything lowercase
            
            if pinput in ['quit', 'exit']:
                print(f'{board.turn} quit the game.')
                return 0
            
            move = board.getMove(pinput)
            move_valid = board.move_valid(move)
            print(move_valid)
            
        board.move(move)
               
# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
