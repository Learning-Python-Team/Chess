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
                square.set_piece('White', 'Pawn')
            
            if square.column == 0 or square.column == 7:
                if square.column == 7:
                    color = 'Black'
                else:
                    color = 'White'
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

class Move:
    def __init__(self):
        self.top = 
        self.bottom =
        self.right =
        self.left =
        self.diagonal_top_right = 
        self.diagonal_top_left = 
        self.diagonal_bottom_right = 
        self.diagonal_bottom_left =

    def move_piece(self, square):
        pass
        # the current idea is to set the origin squares piece to none, none and the target piece to the origin piece.
        # if im not mistaken that also resolves the need for a 'schlagen/attack' class/function

    def can_move(self, square):
        if square.role == 'Pawn':
            if square.color == 'black':
                if diagonal_bottom_right.column or diagonal_bottom_left.column == square.column -1
            else:



    def possible_moves(self, row, column, color, role):#, diagonal_check):
        pass # this function is going to calculate the possible moves of a chesspiece. 
             # it is planned to only calculate for the chesspiece that is going to be moved.
             # another possibility is to calculate for the whole board, and add a string of possibilities
             # to a second list or the squares. i want to avoid that if possible, though it would make it possible 
             # to display possible moves when selecting a chesspiece. 
             # this possible implementation is more likely to be applied in the ui version though.
        

def main():
    Board()

if __name__ == '__main__':
    main()