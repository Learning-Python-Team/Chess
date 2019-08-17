# parent class for all pieces
class __Piece:
    def __init__(self, color, moved=False):
        self.color = color
        self.wsymbols = ['☐', '♟', '♜', '♞', '♝', '♛', '♚']  # allows for easy remapping of the symbols
        self.bsymbols = ['☐', '♙', '♖', '♘', '♗', '♕', '♔']
        self.moved = moved


class NonePiece(__Piece):
    def __init__(self):
        super().__init__(None, moved=None)
        if self.color == 'white':
            self.symbol = self.wsymbols[0]
        else:
            self.symbol = self.bsymbols[0]
        

class Pawn(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[1]
        else:
            self.symbol = self.bsymbols[1]
        self.vectors = [(1, 0), (1, 1), (1, -1)]
        

class Rook(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[2]
        else:
            self.symbol = self.bsymbols[2]
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


class Knight(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[3]
        else:
            self.symbol = self.bsymbols[3]
        self.vectors = [(1, 2), 
                        (1, -2), 
                        (-1, 2), 
                        (-1, -2),
                        (2, 1),
                        (2, -1),
                        (-2, 1),
                        (-2, -1)]
        
        
class Bishop(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[4]
        else:
            self.symbol = self.bsymbols[4]
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
        
        
class Queen(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[5]
        else:
            self.symbol = self.bsymbols[5]
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
        
        
class King(__Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.symbol = self.wsymbols[6]
        else:
            self.symbol = self.bsymbols[6]
        self.vectors = [(1, 0), 
                        (-1, 0), 
                        (0, 1), 
                        (0, -1), 
                        (1, 1), 
                        (1, -1), 
                        (-1, 1), 
                        (-1, -1)]
