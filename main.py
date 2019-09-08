import argparse
import chess_text
import chess_gui

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-t', '--text', help='Starts the chess programm in terminal mode.', action='store_true')
    args = argparser.parse_args()
    
    if args.text:
        chess_text.main()
    else:
        chess_gui.main()
        
if __name__ == '__main__':
    main()
