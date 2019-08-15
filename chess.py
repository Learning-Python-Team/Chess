# Note from Alex - I think it would be worth adding comments throughout this code so beginners can follow!
# Also, I'm realised I'm not good enough at Python to contribute to this!
# Need to get to grips with OOP!

# Note from Zero - Thats why were doing this: to learn together!
# further Comments and explanations will be added soon


class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.piece = NonePiece()

# the board class contains a list of square objects, as well as the function to initially set the board up, 
# and the function for moving the pieces on the board

class Board:
    def __init__(self):
        self.board = []

        for row in range(8):
            for column in range(8):
                self.board.append(Square(row, column))  # generates a 1-dimensional list of square objects

        self.setup()  # populates the board with the initial setup of pieces

    def setup(self):
        for square in self.board:
            if square.column == 1 or square.column == 6:
                if square.column == 1:
                    square.piece = Pawn('white')
                else:
                    square.piece = Pawn('black')

            if square.column == 0 or square.column == 7:
                if square.column == 7:
                    color = 'black'
                else:
                    color = 'white'

                if square.row == 0 or square.row == 7:
                    square.piece = Rook(color)
                if square.row == 1 or square.row == 6:
                    square.piece = Knight(color)
                if square.row == 2 or square.row == 5:
                    square.piece = Bishop(color)
                if square.row == 3:
                    square.piece = Queen(color)
                if square.row == 4:
                    square.piece = King(color)

    def move(self, origin, destination):  # 'moves' the pieces on the board
        pass


def move_valid(move):
    """
    tests wether or not the move specified is a valid move
    """
    return True





### Pieces from here on out ###

# parent class for all pieces
class Piece:
    def __init__(self, color):
        self.color = color


class NonePiece(Piece):
    def __init__(self):
        # The movement vectors of the piece.
        # The format for the vector is as follows: ((fwd, bwd), (left, right), can_capture: bool)
        super().__init__(None)
        self.vectors = None
        self.collision = None
        self.backwards = None


class Pawn(Piece):
    def __init__(self, color):
        # The format for the vector is as follows: ((fwd, bwd), (left, right), can_capture: bool)
        super().__init__(color)
        self.vectors = [((1, 0), (0, 0), False), ((1, 1), (0, 0), True)]
        self.collision = True
        self.backwards = False


# class for players and turns (not very useful now, but very nice for integration in discord and the like)
class Players:
    def __init__(self, player1, player2):
        self.white = 'white'  # player1
        self.black = 'black'  # player2
        self.turn = self.white

# The loop the game runs in. It takes a user input, checks that input for validity, 
# and executes that input if it is valid. It terminates once the game is won or a player quits the game
def main():
    players = Players('white', 'black')
    board = Board()

    while True:
        # makes the input loop run at least once
        move_valid = False
        pinput = input(f'{players.turn}: ')
        while not move_valid:
            move_valid = move_valid(pinput)
            if not move_valid:
                print(f'The move \'{pinput}\' is not a valid move.')
                pinput = input(f'{players.turn}: ')

        if pinput in ['quit', 'exit']:
            print(f'{players.turn} quit the game.')
            return

        print('imagine fancy ascii board here')

# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
