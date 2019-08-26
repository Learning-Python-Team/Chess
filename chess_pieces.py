# parent class for all pieces
WHITE = "White"
BLACK = "Black"
KNIGHTS = ['♞', '♘']
WSYMBOLS = ['☐', '♟', '♜', '♞', '♝', '♛', '♚']
BSYMBOLS = ['☐', '♙', '♖', '♘', '♗', '♕', '♔']

class __Piece:
    def __init__(self, color, moved=False):
        self.color = color
        self.moved = moved

class NonePiece(__Piece):
    def __init__(self):
        super().__init__(None, moved=None)
        self.color = None  # doesn't really make sense
        self.symbol = WSYMBOLS [0]
        if self.color == WHITE:
            self.symbol = WSYMBOLS[0]
        else:
            self.symbol = BSYMBOLS[0]
            
        self.vectors = None
        
    def __str__(self): return self.symbol
        

class Pawn(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == WHITE:
            self.symbol = WSYMBOLS[1]
        else:
            self.symbol = BSYMBOLS[1]
            
        self.vectors = [(1, 0), (1, 1), (1, -1)]

    def __str__(self): return self.symbol
  

class Rook(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == WHITE:
            self.symbol = WSYMBOLS[2]
        else:
            self.symbol = BSYMBOLS[2]
            
        self.vectors = [(-7, 0),
                        (-6, 0),
                        (-5, 0),
                        (-4, 0),
                        (-3, 0),
                        (-2, 0),
                        (-1, 0),
                        (1, 0),
                        (2, 0),
                        (3, 0),
                        (4, 0),
                        (5, 0),
                        (6, 0),
                        (7, 0),
                        (0, -7),
                        (0, -6),
                        (0, -5),
                        (0, -4),
                        (0, -3),
                        (0, -2),
                        (0, -1),
                        (0, 1),
                        (0, 2),
                        (0, 3),
                        (0, 4),
                        (0, 5),
                        (0, 6),
                        (0, 7)]

    def __str__(self): return self.symbol


class Knight(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == WHITE:
            self.symbol = WSYMBOLS[3]
        else:
            self.symbol = BSYMBOLS[3]
            
        self.vectors = [(1, 2), 
                        (1, -2), 
                        (-1, 2), 
                        (-1, -2),
                        (2, 1),
                        (2, -1),
                        (-2, 1),
                        (-2, -1)]

    def __str__(self): return self.symbol
   
        
class Bishop(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == WHITE:
            self.symbol = WSYMBOLS[4]
        else:
            self.symbol = BSYMBOLS[4]
            
        self.vectors = [(-7, -7),
                        (-6, -6),
                        (-5, -5),
                        (-4, -4),
                        (-3, -3),
                        (-2, -2),
                        (-1, -1),
                        (1, 1),
                        (2, 2),
                        (3, 3),
                        (4, 4),
                        (5, 5),
                        (6, 6),
                        (7, 7)]

    def __str__(self): return self.symbol

        
class Queen(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == WHITE:
            self.symbol = WSYMBOLS[5]
        else:
            self.symbol = BSYMBOLS[5]
            
        self.vectors = [(-7, 0),
                        (-6, 0),
                        (-5, 0),
                        (-4, 0),
                        (-3, 0),
                        (-2, 0),
                        (-1, 0),
                        (1, 0),
                        (2, 0),
                        (3, 0),
                        (4, 0),
                        (5, 0),
                        (6, 0),
                        (7, 0),
                        (-7, -7),
                        (-6, -6),
                        (-5, -5),
                        (-4, -4),
                        (-3, -3),
                        (-2, -2),
                        (-1, -1),
                        (1, 1),
                        (2, 2),
                        (3, 3),
                        (4, 4),
                        (5, 5),
                        (6, 6),
                        (7, 7)]

    def __str__(self): return self.symbol
        
        
class King(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == WHITE:
            self.symbol = WSYMBOLS[6]
        else:
            self.symbol = BSYMBOLS[6]
            
        self.vectors = [(1, 0), 
                        (-1, 0), 
                        (0, 1), 
                        (0, -1), 
                        (1, 1), 
                        (1, -1), 
                        (-1, 1), 
                        (-1, -1)]


    def __str__(self): return self.symbol
