import pprint
import itertools

pprint.PrettyPrinter(indent=4)



class Chess:
    def __init__ (self):
        pass
    
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
        

def main():
    Board()

if __name__ == '__main__':
    main()