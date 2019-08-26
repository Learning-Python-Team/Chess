from chess_pieces import *
import re
import logging 

logging.getLogger().setLevel(logging.WARNING)

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
            board = self.game_board
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

    def mirror(self): 
        logging.debug ("Flipping the board")
        # Make sure we don't change the actual board
        board = self.game_board.copy()

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

    def move(self, move):
        """
        Moves the pieces from one square to another.
        Requires move to be of form: ( 
            (origin_row, origin_col), 
            (destination_row, destination_col)
        )
        """
        logging.info(f"Moving piece from {move.origin} to {move.target}")

        self [move.origin].moved = True
        self [move.target] = self [move.origin]
        self [move.origin] = NonePiece()

        # changing the player whose turn it is
        if self.turn == WHITE: self.turn = BLACK
        else: self.turn = WHITE
        logging.info(f"Switching turn to {self.turn}")

    def interpolate(origin: tuple, offset: tuple):
        """
        Returns a generator that yields every square from origin 
        until it reaches the square targeted by offset.
        """
        # Decide how to interpolate vertically
        if offset [0] == 0: vertical = 0
        elif offset [0] > 0: vertical = 1
        else: vertical = -1

        # Decide how to interpolate horizontally
        if offset [1] == 0: horizontal = 0
        elif offset [1] > 0: horizontal = 1
        else: horizontal = -1

        progress = (0, 0)
        direction = (vertical, horizontal)
        while True: 
            origin = add_tuples (origin, direction)
            progress = add_tuples (progress, direction)
            if progress == offset: return
            else: yield origin

    def move_valid(self, move):
        """
        Tests whether or not the move specified is a valid move
        We need to check 4 things: 
            1. That we're moving the piece of our color
            2. That we're moving it to a valid position (based on piece type)
            3. That we are/are not colliding with our own piece at the target
            4. There's nothing in the way (except when we're moving the knight)
        """

        if self [move.origin].color != self.turn: return False
        elif move.vector not in self [move.origin].vectors: return False
        elif self [move.target].color == self.turn: return False
        # Now check if there is anything in the way.
        elif self [move.origin].symbol in KNIGHTS: return True  # doesn't apply
        else: return all (  # make sure all squares in the way are empty
            self [pos].color is None
            for pos in Board.interpolate(move.origin, move.vector)
        )

        # def autolistrange(value):
        #     if value < 0:
        #         return list(range(-1, value, -1))
        #     else:
        #         return list(range(1, value, 1))
            
        # # tests
        # def check(i, vector_int):
        #     if vector_int == 0:
        #         # if the square is not empty
        #         if not isinstance(relative_piece(i, 0), NonePiece):
                    
        #             # checks wether the piece is the players own color
        #             if relative_piece(i, 0).color == self.turn:
                    
        #             # checks wether i is the last step of the vector (capturing a piece)
        #             if i == len(range(0, vector[vector_int], -1)):
        #                 return True
                    
        #             return False
            
        #         else: return True
            
        #     elif vector_int == 1:
        #         # checks whether the square is not empty
        #         if not isinstance(relative_piece(0, i), NonePiece):
                    
        #             # checks wether the piece is the players own color
        #             if relative_piece(0, i).color == WHITE and self.turn == WHITE:
        #                 return False
        #             elif relative_piece(0, i).color == WHITE and self.turn == BLACK:
        #                 return False
                    
        #             # checks wether i is the last step of the vector (capturing a piece)
        #             if i == len(range(0, vector[vector_int], -1)):
        #                 return True
                    
        #             return False
                
        #         return True
        
        # def test_vertical():
        #     if vector[0] == 0:
        #         return True
            
        #     elif vector[0] == 1:
        #         checkval = check(vector[0], 1)
        #         if not checkval:
        #             return False
        #         else:
        #             return True
        #     else:
        #         for i in autolistrange(vector[0]):
        #             checkval = check(i, 1)
        #             if not checkval:
        #                 return False
        #             else:
        #                 return True
        
        # def test_horiziontal():
        #     if vector[1] == 0:
        #         return True
            
        #     elif vector[1] == 1:
        #         checkval = check(vector[1], 0)
        #         if not checkval:
        #             return False
        #         else:
        #             return True
        #     else:
        #         for i in autolistrange(vector[1]):
        #             checkval = check(i, 0)
        #             if not checkval:
        #                 return False
        #             else:
        #                 return True
         
        # def test_diagonal():
        #     lst_row = autolistrange(vector[0])
        #     lst_col = autolistrange(vector[1])
            
        #     ziplist = zip(lst_row, lst_col)
            
        #     for i,j in ziplist:
        #         if not isinstance(relative_piece(i, j), NonePiece):
        #                 if relative_piece(i, j).color == WHITE and self.turn == WHITE:
        #                     return False
        #                 elif relative_piece(i, j).color == WHITE and self.turn == BLACK:
        #                     return False
                        
        #                 if (i,j) == (vector[0],vector[1]):
        #                     return True
        #                 else:
        #                     return False

        # # applying tests
        # # TODO: integrate non-standard moves like the rochade
        # # TODO: test_diagonal is buggy!
        # if origin_piece.color == WHITE and self.turn != WHITE:
        #     return False
        # elif origin_piece.color == WHITE and self.turn != BLACK:
        #     return False
        
        # if isinstance(origin_piece, Pawn):
        #     if self.turn == WHITE:
        #         logging.debug('runs')
        #         if vector == origin_piece.vectors[0] and isinstance(relative_piece(1, 0), NonePiece):
        #             logging.debug('runsa')
        #             return True
        #         elif vector in origin_piece.vectors[1:3] and not isinstance(relative_piece(1, vector[1]), NonePiece):
        #             logging.debug('runsb')
        #             return True
        #         else:
        #             logging.debug('runsc')
        #             return False
                
        #     else:
        #         if vector == origin_piece.vectors[0] and isinstance(relative_piece(-1, 0), NonePiece):
        #             return True
        #         elif vector in origin_piece.vectors[1:3] and not isinstance(relative_piece(-1, vector[1]), NonePiece):
        #             return True
        #         else:
        #             return False
            
        # elif isinstance(origin_piece, Rook):
        #     if vector in origin_piece.vectors:
        #         return test_horiziontal() and test_vertical()
        
        # elif isinstance(origin_piece, Knight):
        #     if vector in origin_piece.vectors:
        #         return True
            
        # elif isinstance(origin_piece, Bishop):
        #     if vector in origin_piece.vectors:
        #         return test_diagonal()
        
        # elif isinstance(origin_piece, Queen):
        #     if vector in origin_piece.vectors:
        #         return test_horiziontal() and test_vertical() and test_diagonal()
        
        # elif isinstance(origin_piece, King):
        #     if vector in origin_piece.vectors:
        #         return test_horiziontal() and test_vertical() and test_diagonal()
                     
        # return False

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
        return Move (origin, destination, flip = self.turn == WHITE) 

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
                move_valid = board.move_valid(move)
            if not move_valid:
                print(f'Move [{pinput}] is not valid.')
                
            logging.debug(f"Move valid? {move_valid}")
            
        board.move(move)
               
# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
