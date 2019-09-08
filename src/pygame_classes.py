from src.board import Board
from src.chess_pieces import *
import pygame

class ChessGame:
    def __init__ (self, window, width, height, checkersize):
        self.window = window
        self.width = width
        self.height =  height
        self.CHECKERSIZE = checkersize
        
        self.board = Board()
        
    
    def redrawWindow(self):
        self.draw_checkerboard()
        self.draw_pieces()
        
    def draw_checkerboard(self):
        color = None
        color_w = (240,216,161)
        color_b = (115,58,0)
        
        board = list(reversed(self.board.game_board.copy()))
        
        y=0
        for row in board:
            
            # determine color offset for this row
            if board.index(row)%2 == 0: color = color_w
            else: color = color_b
            
            x = 0
            for square in row:
                square.color = color
                square.coords = (x,y)  # Important to know where to blit the images to
                self.draw_chessrect((x,y), color)
                
                # inverting color for the next iteration so it doesnt print a black/white line
                if color == color_w: color = color_b
                else: color = color_w
            
            # increment coordinates that get embedded in square.coords
                x += self.width / 8
            y += self.height / 8
    
    def draw_chessrect(self, coords: tuple, color: tuple):
        pygame.draw.rect(self.window, color, (coords, self.CHECKERSIZE))
    
    def draw_pieces(self):
        # uses surface.blits to mass-blit the pieces
        blitsequence = []
        for row in self.board.game_board:
            for square in row:
                imgtuples = self.get_imgtuples(square)
                if imgtuples is not None: blitsequence.append(imgtuples)
        blitsequence = tuple(blitsequence)
        self.window.blits(blitsequence)
                
    
    def get_imgtuples(self, square):
        # gets a tuple of pimage and coords necessary for window.blits
        if type(square.piece) == NonePiece:
            return
        pimage = self.get_image_surf(square.piece)
        coords = (square.coords[0]+6.25, square.coords[1]+6.25)  # offset of the piece TODO: adjust to middle
        size = (self.CHECKERSIZE[0]-14,self.CHECKERSIZE[1]-14)
        pimage = pygame.transform.scale(pimage, size)
        return pimage, coords
        
    def get_image_surf(self, piece):
        # construct path to png
        PIECEDIR = 'src/Pieces/'
        profs = [Pawn, Rook, Bishop, Knight, Queen, King]
        profstrs = ['p', 'r', 'b', 'n', 'q', 'k']
        for index in range(6):
            if type(piece) == profs[index]:
                profession_char = profstrs[index]
        if piece.color == WHITE: color_str = 'white'
        else: color_str = 'black'
        # returns image surface
        return pygame.image.load(f'{PIECEDIR}{color_str}_{profession_char}.png')
    
        
class Button:
    def __init__ (self, colors, x, y, width, height, text='', toggle=False):
        # colors is tuple consisting of a initial rgb tuple, and a mouseover rgb tuple which is the toggle tuple if toggle is True
        self.colors = colors
        # The color the Button is currently drawn in
        self.color = colors[0]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        # If the button can be toggled, and the current toggle state
        self.toggle = toggle
        self.toggled = False

    def draw(self, win, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def check(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_over(pos):
                if self.toggle:
                    if self.toggled:
                        self.color = self.colors[0]
                        self.toggled = False
                    else:
                        self.color = self.colors[1]
                        self.toggled = True
                    return self.toggled
                else:
                    return True
                        
        if event.type == pygame.MOUSEMOTION:
            if not self.toggle:
                if self.is_over(pos):
                    self.color = self.colors[1]
                else:
                    self.color = self.colors[0]

