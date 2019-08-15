from chess_pieces import *


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

        for column in range(8):
            self.board.append([])
            for row in range(8):
                self.board[column].append(Square(row, column))  # generates a 2-dimensional list of square objects

        self.setup()  # populates the board with the initial setup of pieces
        print(self.board[0])
        for item in self.board[0]:
            print(item.piece)
                
    def setup(self):
        for row in self.board:
            for square in row:
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
    
    def move_valid(self, move):
        """
        tests wether or not the move specified is a valid move
        """
        return True

    def draw(self):  # doesnt look nice, but makes debugging helluvalot easier
        for rows in self.board:
            print('  |')
            for square in rows:
                piece = square.piece.symbol
                startchar = ' '
                endchar = ''
                if square.row == 7:
                    endchar = '\n'
                elif square.row == 0:
                    startchar = f'{square.column+1} | '
                    
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


def main():
    '''
    The loop the game runs in.
    It takes a user input, checks that input for validity, and calls move on it if it is valid.
    It terminates once the game is won or a player quits the game.
    '''
    players = Players('white', 'black')
    board = Board()
#DEBUG
    board.draw()
    while True:
        # makes the input loop run at least once
        move_valid = False
        pinput = input(f'{players.turn}: ')
        while not move_valid:
            move_valid = board.move_valid(pinput)
            if not move_valid:
                print(f'The move \'{pinput}\' is not a valid move.')
                pinput = input(f'{players.turn}: ')

        if pinput in ['quit', 'exit']:
            print(f'{players.turn} quit the game.')
            return

        board.draw()

# Makes sure, that the game only runs when it is not being imported.
if __name__ == '__main__':
    main()
