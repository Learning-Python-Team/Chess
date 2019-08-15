# parent class for all pieces
class __Piece:
    def __init__(self, color, collision=True, backwards=True):
        self.color = color
        self.collision = collision  # whether or not the piece is able to move past an enemy piece without collecting it (only occurence is the Knight)
        self.backwards = backwards  # whether or not the piece is able to move backwards (only occurence is the Pawn)
        self.wsymbols = ['☐', '♟', '♜', '♞', '♝', '♛', '♚']  # allows for easy remapping of the symbols
        self.bsymbols = ['☐', '♙', '♖', '♘', '♗', '♕', '♔']


class NonePiece(__Piece):
    def __init__(self):
        super().__init__(None, collision=None, backwards=None)
        if self.color == 'white':
            self.symbol = self.wsymbols[0]
        else:
            self.symbol = self.bsymbols[0]
        

class Pawn(__Piece):
    def __init__(self, color):
        super().__init__(color, backwards=False)
        if self.color == 'white':
            self.symbol = self.wsymbols[1]
        else:
            self.symbol = self.bsymbols[1]
        

class Rook(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[2]
        else:
            self.symbol = self.bsymbols[2]


class Knight(__Piece):
    def __init__(self, color):
        super().__init__(color, collision=False)
        if self.color == 'white':
            self.symbol = self.wsymbols[3]
        else:
            self.symbol = self.bsymbols[3]
        
        
class Bishop(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[4]
        else:
            self.symbol = self.bsymbols[4]
        
        
class Queen(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[5]
        else:
            self.symbol = self.bsymbols[5]
        
        
class King(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[6]
        else:
            self.symbol = self.bsymbols[6]
