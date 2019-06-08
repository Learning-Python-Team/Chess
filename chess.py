import pprint

pprint.PrettyPrinter(indent=4)



    
class Board:
    def __init__ (self):
        self.board = []
        
        for row in range(8):
            for column in range (8):
                self.board.append(Square(row, column))
        
        print('A board with the size of ' + str(len(self.board)) + ' spaces  has been generated.')
        
        self.setup()

        

    def setup(self):
        for square in self.board:
            if square.column == 1 or square.column == 6:
                square.set_piece('white', 'Pawn')
            
            if square.column == 0 or square.column == 7:
                if square.column == 7:
                    color = 'black'
                else:
                    color = 'white'
                if square.row == 0 or square.row == 7:
                    square.set_piece(color, 'Rook')
                if square.row == 1 or square.row == 6:
                    square.set_piece(color, 'Knight')
                if square.row == 2 or square.row == 5:
                    square.set_piece(color, 'Bishop')
                if square.row == 3:
                    square.set_piece(color, 'Knight')
                if square.row == 4:
                    square.set_piece(color, 'King')
            
            #pprint.pprint(square.get_attributes())
    
    #this will most likely be implemented in a movement class
    # def possible_moves(self, row, column, color, role):#, diagonal_check):
    #     pass #this function is going to calculate the possible moves of a chesspiece. 
    #          #it is planned to only calculate for the chesspiece that is going to be moved.
        
        


class Square:
    def __init__ (self, row, column):
        self.row = row
        self.column = column
        self.piece = Piece(None, None)
    
    def set_piece (self, color, role):
        self.piece = Piece(color, role)

    def empty_square (self):
        self.piece = Piece(None, None)

    def get_attributes(self):
        return 'row: ', str(self.row), 'column: ', str(self.column), 'color: ', str(self.piece.color), 'role: ', str(self.piece.role)



class Piece:
    def __init__(self, color, role):
        self.color = color
        self.role = role

class Pawn(Piece): # How!?!?!?
    def __init__(self, square):
        self.square = square.Square
        





class Move:
    def __init__(self, row, column):
        pass

    def move_piece(self, square):
        pass

    def can_move(self, square, move_row, move_column): # currently trying to remake this into classes, since this doesnt really seem to be a good way to go about things

        # None Type (to prevent None Type pieces from being moved, needs to be at the top)
        if square.role == None:
            return False
        
        # Pawns
        #ToDo: add diagonal movement if pieces, prevent straightt movement of pieces if another piece blocks the path 
        if sqare.role == 'Pawn':
            if square.color == 'black':
                for row in Board.board:
                    
                    if move_row == square.row-1:
                        if move_column == square.column-1 or move_column == square.column +1:
                            for column in Board.board:
                                pass

                        return True
                    if square.row == 6 & move_row == square.row-2:
                        return True
                    else:
                        return False
            else: 
                for row in Board.board:
                    if move_row == square.row+1:
                        return True
                    if square.row == 1 & move_row == square.row+2:
                        return True
                    else:
                        return False

        # Rooks 
        #ToDo: implement the king and rook switching places if neither of them have moved since beginning of the match
        if sqare.role == 'Rook':


            if square.color == 'black':
                for row in Board.board:
                    if move_row == square.row or move_column == square.column:
                        return True
                    else:
                        return False
            else:
                return False





        

def main():
    Board()

if __name__ == '__main__':
    main()