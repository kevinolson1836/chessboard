import Custom_Chessboard_Square as ccs
import chess
import chess.svg

DEBUG = 1

BOARD = chess.Board()

I2C_ADDRESS = [
    
    [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08],
    [0x09,0x10,0x11,0x12,0x13,0x14,0x15,0x16],
    [0x17,0x18,0x19,0x20,0x21,0x22,0x23,0x24],
    [0x25,0x26,0x27,0x28,0x29,0x30,0x31,0x32],
    [0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x40],
    [0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48],
    [0x49,0x50,0x51,0x52,0x53,0x54,0x55,0x56],
    [0x57,0x58,0x59,0x60,0x61,0x62,0x63,0x64],
    
    ]


CHESS_SQUARES = []


def main():
    global BOARD

    init_chess_squares(BOARD)
    print_board_and_display(BOARD)

def init_chess_squares(BOARD):
    square_count = 0
    temp_list = []

    # loop so we can generate a x y cord grid....
    for x in range(8):            
            for y in range(8):    

                # init the squares
                square = ccs.Custom_Square(
                    BOARD=BOARD,
                    I2C_ADDRESS=I2C_ADDRESS[x][y], 
                    SQUARE_NAME=chess.SQUARE_NAMES[square_count],
                    SQUARE_ID=chess.SQUARES[square_count],
                )
                
                square_count = square_count + 1     # loop count
                temp_list.append(square)            # temp list to hold 8 squares

                # if temp list is 8 squares long append it to the main CHESS_SQUARES list to keep the x y grid in tact
                if (square_count % 8 == 0):
                    CHESS_SQUARES.append(temp_list)
                    temp_list = []

                # DEBUG 
                if DEBUG:
                    square.print_debug_data()

    # DEBUG 
    if DEBUG:
        square.print_board()

def print_board_and_display(BOARD):
    print(BOARD)
    svg = chess.svg.board(BOARD)
    with open("board.svg", "w") as f:
        f.write(svg)



if __name__ == "__main__":
    main()
