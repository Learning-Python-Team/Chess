import argparse
import chess_text

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-t', '--text', help='Starts the chess programm in terminal mode.', action='store_true')
    args = argparser.parse_args()
    
    if args.text:
        chess_text.main()
    else:
        print('The GUI is not implemented yet. Start the game with -t or --text to use terminal mode.')
        return
        
if __name__ == '__main__':
    main()
