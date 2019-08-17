from chess_pieces import *
import re

class Square:
    '''
    The Dataclass the board is 'made' of
    '''
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.piece = NonePiece()


class Board:
    '''
    The board class contains a list of square objects, as well as the function to initially set the board up, 
    and the function for moving the pieces on the board.
    '''
    def __init__(self):
        self.board = []

        for row in range(8):
            self.board.append([])
            for column in range(8):
                self.board[row].append(Square(row, column))  # generates a 2-dimensional list of square objects

        self.setup()  # populates the board with the initial setup of pieces
                
    def setup(self):
        for row in self.board:
            for square in row:
                if square.row == 1 or square.row == 6:
                    if square.row == 1:
                        square.piece = Pawn('white')
                    else:
                        square.piece = Pawn('black')

                if square.row == 0 or square.row == 7:
                    if square.row == 7:
                        color = 'black'
                    else:
                        color = 'white'

                    if square.column == 0 or square.column == 7:
                        square.piece = Rook(color)
                    if square.column == 1 or square.column == 6:
                        square.piece = Knight(color)
                    if square.column == 2 or square.column == 5:
                        square.piece = Bishop(color)
                    if square.column == 3:
                        square.piece = Queen(color)
                    if square.column == 4:
                        square.piece = King(color)

    def move(self, move):
        '''
        'moves' the pieces on the board
        '''
        
        # unpacking tuples
        origin_row = move[0][0]
        origin_column = move[0][1]
        
        destination_row = move[1][0]
        destination_column = move[1][1]
        
        
        # print(move)
        # print(self.board[0][0].piece)
        # print(self.board[1][0].piece)
        
        # getting piece objects from self.board
        origin_piece = self.board[origin_row][origin_column].piece
        destination_piece = self.board[destination_row][destination_column].piece
        
        # set the moved attrubute of the origin piece to True (needed for castling)
        self.board[origin_row][origin_column].piece.moved = True
        
        # sets the piece attribute of the destination square to the piece attrubute of the origin square.
        # havent tested it, but pretty sure not using origin_piece would create a dependency between the objects here.
        self.board[destination_row][destination_column].piece = origin_piece
        
        # Implement rules for castling here.
        
        self.board[origin_row][origin_column].piece = NonePiece()
        
        # print(self.board[0][0].piece)
        # print(self.board[1][0].piece)
        
    def move_valid(self, move, players):
        """
        tests wether or not the move specified is a valid move
        """
        origin_row = move[0][0]
        origin_column = move[0][1]
        
        destination_row = move[1][0]
        destination_column = move[1][1]
        
        vector = (destination_row - origin_row, destination_column - origin_column)
                  
        origin_piece = self.board[origin_row][origin_column].piece
        destination_piece = self.board[destination_row][destination_column].piece
        
        def relative_piece(row, column):
            return self.board[origin_row+row][origin_column+column].piece
        
        # tests
        def check(i, vector_int, players):
            if vector_int == 0:
                if not isinstance(relative_piece(i, 0), NonePiece):
                    if relative_piece(i, 0).color == 'white' and players.turn == players.white:
                        return False
                    if relative_piece(i, 0).color == 'black' and players.turn == players.black:
                        return False
                    
                    if i == len(range(0, vector[vector_int], -1)):
                        return True
                    else:
                        return False
                return True
            elif vector_int == 1:
                if not isinstance(relative_piece(0, i), NonePiece):
                    if relative_piece(0, i).color == 'white' and players.turn == players.white:
                        return False
                    elif relative_piece(0, i).color == 'black' and players.turn == players.black:
                        return False
                    
                    if i == len(range(0, vector[vector_int], -1)):
                        return True
                    else:
                        return False
                return True
            raise WrongVectorIntException
            
        def test_vertical(players):
            if vector[0] == 0:
                return True
            
            if vector[0] < 0:
                for i in range(0, vector[0], -1):
                    checkval = check(i, 0, players)
                    if not checkval:
                        return False
                return True
            
            else:
                for i in range(vector[0]):
                    checkval = check(i, 0, players)
                    if not checkval:
                        return False
                return True
            return True
        
        def test_horiziontal(players):
            if vector[1] == 0:
                return True
            
            if vector[1] < 0:
                for i in range(0, vector[1], -1):
                    checkval = check(i, 1, players)
                    if not checkval:
                        return False
                return True
            
            else:
                for i in range(vector[1]):
                    checkval = check(i, 1, players)
                    if not checkval:
                        return False
                return True
            return True
        
        def test_diagonal(players):
            if vector[0] < 0 and vector[1] < 0:
                for i in range(0, vector[0], -1):
                    if not isinstance(relative_piece(i, i), NonePiece):
                        if relative_piece(i, i).color == 'white' and players.turn == players.white:
                            return False
                        elif relative_piece(i, i).color == 'black' and players.turn == players.black:
                            return False
                        
                        if i == len(range(0, vector[0], -1)):
                            return True
                        else:
                            return False
                        
            elif vector[0] < 0 and vector[1] > 0:
                lst_row = list(range(0, vector[0], -1))
                lst_col = list(range(vector[1]))
                lst_zip = zip(lst_row, lst_col)
                for i,j in lst_zip:
                    if not isinstance(relative_piece(i, j), NonePiece):
                        if relative_piece(i, j).color == 'white' and players.turn == players.white:
                            return False
                        elif relative_piece(i, j).color == 'black' and players.turn == players.black:
                            return False
                        
                        if i == len(lst_row):
                            return True
                        else:
                            return False
            
            elif vector[0] > 0 and vector[1] < 0:
                lst_row = list(range(vector[0]))
                lst_col = list(range(0, vector[1], -1))
                lst_zip = zip(lst_row, lst_col)
                for i,j in lst_zip:
                    if not isinstance(relative_piece(i, j), NonePiece):
                        if relative_piece(i, j).color == 'white' and players.turn == players.white:
                            return False
                        elif relative_piece(i, j).color == 'black' and players.turn == players.black:
                            return False
                        
                        if i == len(lst_row):
                            return True
                        else:
                            return False
                        
            else:
                for i in range(vector[0]):
                    if not isinstance(relative_piece(i, i), NonePiece):
                        if relative_piece(i, i).color == 'white' and players.turn == players.white:
                            return False
                        elif relative_piece(i, i).color == 'black' and players.turn == players.black:
                            return False
                        
                        if i == len(range(vector[0])):
                            return True
                        else:
                            return False
        
        # applying tests
        # TODO: integrate non-standard moves like the rochade
        if origin_piece.color == 'white' and players.turn != players.white:
            return False
        elif origin_piece.color == 'black' and players.turn != players.black:
            return False
        
        if isinstance(origin_piece, Pawn):
            if vector == origin_piece.vectors[0] and isinstance(relative_piece(1, 0), NonePiece):
                return True
            elif vector in origin_piece.vectors[1:2] and not isinstance(relative_piece(1, vector[1]), NonePiece):
                return True
            else:
                return False
            
        elif isinstance(origin_piece, Rook):
            if vector in origin_piece.vectors:
                return test_horiziontal(players) and test_vertical(players)
        
        elif isinstance(origin_piece, Knight):
            if vector in origin_piece.vectors:
                return True
            
        elif isinstance(origin_piece, Bishop):
            if vector in origin_piece.vectors:
                return test_diagonal_r(players) and test_diagonal_l(players)
        
        elif isinstance(origin_piece, Queen):
            if vector in origin_piece.vectors:
                return test_horiziontal(players) and test_vertical(players) and test_diagonal_r(players) and test_diagonal_l(players)
        
        elif isinstance(origin_piece, King):
            if vector in origin_piece.vectors:
                return test_horiziontal(players) and test_vertical(players) and test_diagonal_r(players) and test_diagonal_l(players)
                     
        return False

    def draw(self, players):  # doesnt look nice, but makes debugging helluvalot easier.
        if players.turn == players.white:
            board_lst = reversed(self.board)
        else:
            board_lst = self.board
        for rows in board_lst:
            print('  |')
            for square in rows:
                piece = square.piece.symbol
                startchar = ' '
                endchar = ''
                if square.column == 7:
                    endchar = '\n'
                elif square.column == 0:
                    startchar = f'{square.row+1} | '
                    
                print(f'{startchar} {piece}  ', end=endchar)
        print('¯¯T¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n'
            '  |  a    b    c    d    e    f    g    h')


class Players:
    '''
    Class for players and Turns. (useful for integration in discord and the like)
    '''
    def __init__(self, player1, player2):
        self.white = 'white'  # player1
        self.black = 'black'  # player2
        self.turn = self.white


# parser for player input
def inputparser(str_in):
    char_to_nr_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}   # dict to convert a-h to ints
    matches = re.search(r'([abcdefgh][12345678])\s([abcdefgh][12345678])', str_in)  # regex to match the move out of the input
    if matches is not None:
        origin = matches.group(1)
        origin = (int(origin[1])-1, char_to_nr_dict[origin[0]])  # -1 to fit 0-based indentation
        
        destination = matches.group(2)
        destination = (int(destination[1])-1, char_to_nr_dict[destination[0]])  # -1 to fit 0-based indentation
        
        return origin, destination  # returns a tuple of ((origin_row, origin_column), (destination_row, destination_column))
    
    else: return None  # returns none if the input does not match
        

def main():
    '''
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    '''
    players = Players('white', 'black')
    board = Board()
    
    board.draw(players)
    while True:
        move_valid = False  # makes the input loop run at least 
        move = None
        while not move_valid:
            pinput = input(f'{players.turn}: ').lower()  # .lower() to make everything lowercase
            
            if pinput in ['quit', 'exit']:
                print(f'{players.turn} quit the game.')
                return 0
            
            if pinput == 'draw':
                board.draw(players)
                print(players.turn)
                
            move = inputparser(pinput)
            if move is not None:
                move_valid = board.move_valid(move, players)
            if not move_valid:
                print(f'The move [{pinput}] is not valid.')

               
        # changing the player whose turn it is
        if players.turn == players.white:
            players.turn = players.black
        else:
            players.turn = players.white
            
        board.move(move)
        board.draw(players)

# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
