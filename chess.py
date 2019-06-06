import pprint

pprint.PrettyPrinter(indent=4)



class Chess:
    def __init__ (self):
        pass
    
class Board:
    def __init__ (self):
        # self.board = [[[Square(row, column)]for row in range (8)]for column in range (8)]
        self.board = []
        
        for row in range(8):
            self.board.append([])
            for column in range (8):
                self.board[-1].append(Square(row, column))
        print(pprint.pformat(self.board))

    def setup(self):
        print(pprint.pformat(self.board))
        
        for column in self.board:
            if column == 1:
                self.board[column].append(Square.set_piece('White', 'Pawn'))
                
        
        print(pprint.pformat(self.board))
        print(self.board.row[0][0])
        


class Square:
    def __init__ (self, row, column):
        self.row = row
        self.column = column
        self.piece = None
    
    def set_piece (self, color, role):
        self.piece = Piece(color, role)

    def empty_square (self):
        self.piece = Piece(None, None)


class Piece:
    def __init__(self, color, role):
        self.color = color
        self.role = role
        

def main():
    Board()

if __name__ == '__main__':
    main()