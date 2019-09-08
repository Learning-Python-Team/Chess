from src.chess_pieces import *
import re
import logging

#logging.getLogger().setLevel(logging.DEBUG)

#board_logger = logging.getLogger(__name__)
#board_logger.setLevel(logging.DEBUG)


# small helper functions
def subtract(tup): return tup [0] - tup [1]
def add_tuples(a, b): return tuple (map (sum, zip (a, b)))

class Move: 
    def __init__(self, origin, target, flip): 
        # origin + vector = target
        self.origin = origin
        self.target = target
        self.vector = tuple (map (subtract, zip (origin, target)))
        if flip: self.vector = Move.flip(self.vector)

    def __str__(self): return f"Move from {self.origin} to {self.target}"

    def flip(vector): 
        return -1 * vector [0], -1 * vector [1]

class Square:
    '''
    The Dataclass game_board is 'made' of
    '''
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.default = None
        self.piece = None
        self.reset()

    def __str__(self): return str (self.piece)
    def __repr__(self): return str (self)

    def reset(self): 
        if self.default is None: 
            self.default = NonePiece()
            if self.row == 1: self.default = Pawn(WHITE)
            elif self.row == 6: self.default = Pawn(BLACK)
            elif self.row in (0, 7): 
                color = BLACK if self.row == 7 else WHITE
                if self.column in (0, 7): self.default = Rook(color)
                if self.column in (1, 6): self.default = Knight(color)
                if self.column in (2, 5): self.default = Bishop(color)
                if self.column == 3: self.default = Queen(color)
                if self.column == 4: self.default = King(color)
        self.piece = self.default

class Board:
    '''
    The Board class contains a list of square objects, as well as the function to initially set the game_board up,
    the function to check moves for vaildity,
    and the function for moving the pieces on board.
    '''
    def __init__(self):
        logging.debug ("Setting up board")
        self.game_board = []

        for row in range(8):
            self.game_board.append([])
            for column in range(8):
                self.game_board[row].append(Square(row, column))  # generates a 2-dimensional list of square objects

        self.turn = WHITE

    # These methods will help with getting and setting the pieces
    def __getitem__(self, tup): return self.game_board[tup [0]][tup [1]].piece
    def __setitem__(self, tup, value): 
        self.game_board[tup [0]] [tup [1]].piece = value
    
    def __str__(self):
        # Make sure you are using a monospace font
        result = ""
        if self.turn == WHITE:
            board = reversed(self.game_board)
            indices = range (8, 0, -1)
        elif self.turn == BLACK:
            board = self.mirror()
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
    
    def mirror(self) -> [[str]]: 
        """
        Returns a copy of the board flipped 180 degrees.
        Returns a list of lists of strings
        """

        logging.debug ("Flipping the board")
        # Make sure we don't change the actual board
        board = reversed(self.game_board.copy())

        # First flatten the list
        flat = []
        for row in board: flat.extend(row)
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

    def reset(self): 
        for row in self.game_board:
            for square in row: 
                square.reset()
    
    def move(self, move: Move):
        """
        Moves the pieces from one square to another.
        """
        logging.info(f"Moving piece from {move.origin} to {move.target}")

        self [move.origin].moved = True
        self [move.target] = self [move.origin]
        self [move.origin] = NonePiece()

        # changing the player whose turn it is
        if self.turn == WHITE: self.turn = BLACK
        else: self.turn = WHITE
        logging.info(f"Switching turn to {self.turn}")

    def interpolate(origin: tuple, vector: tuple):
        """
        Returns a generator that yields every square from origin 
        until it reaches the square targeted by vector.
        [origin] and [vector] correspond to the fields of Move.
        """
        # Decide how to interpolate vertically
        if vector [0] == 0: vertical = 0
        elif vector [0] > 0: vertical = 1
        else: vertical = -1

        # Decide how to interpolate horizontally
        if vector [1] == 0: horizontal = 0
        elif vector [1] > 0: horizontal = 1
        else: horizontal = -1

        progress = (0, 0)
        direction = (vertical, horizontal)
        while True: 
            origin = add_tuples (origin, direction)
            progress = add_tuples (progress, direction)
            if progress == vector: return
            else: yield origin

    def is_valid_move(self, move: Move) -> bool:
        """
        Tests whether or not the move specified is a valid move
        We need to check 4 things: 
            1. That we're moving the piece of our color
            2. That we're moving it to a valid position (based on piece type)
            3. That we are/are not colliding with our own piece at the target
            4. There's nothing in the way (except when we're moving the knight)
        """

        return (
            self [move.origin].color == self.turn and
            move.vector in self [move.origin].vectors and
            self [move.target].color != self.turn and
            # Now check if there is anything in the way
            (
                type (self [move.origin]) is Knight or  # doesn't apply
                all (  # make sure all squares in the way are empty
                    type (self [pos]) is NonePiece
                    for pos in Board.interpolate(move.origin, move.vector)
                )
            )
        )
    
    def getMove(self, move: str) -> Move:
        """
        Parses move from str input.
        Move must be of form: 
            (origin_letter)(origin_number) + 
            (destination_letter)(destination_number)
        returns a Move object.
        """

        # Maps a: 0, b: 1, etc.
        letter_to_index = {
            letter: index
            for letter, index in zip("abcdefgh", range (8))
        }

        # Get moves from input
        matches = re.search(r'([abcdefgh][12345678])\s([abcdefgh][12345678])', move)
        if matches is None: return None  # cannot determine move
        origin = matches.group(1)  # origin
        origin = (
            int(origin[1]) - 1,  # get the row
            letter_to_index[origin[0]]  # get the column
        )
        
        destination = matches.group(2)
        destination = (
            int(destination[1]) - 1, 
            letter_to_index[destination[0]]
        ) 

        logging.debug(f"Move {move} interpreted as {(origin, destination)}")
        return Move (origin, destination, flip = self.turn == WHITE)
