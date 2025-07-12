
import chess



class Custom_Square:
    """main handler for my chess squares."""

    def __init__(self,BOARD=-1, I2C_ADDRESS=-1, SQUARE_NAME=-1, SQUARE_ID=-1):
        """
        Initialize a new instance of MyClass.

        Args:
            arg1 (type): Description of arg1
            arg2 (type): Description of arg2
        """

        # todo: add color
        #       add rank

        self.BOARD = BOARD
        self.I2C_ADDRESS = I2C_ADDRESS
        self.SQUARE_NAME = SQUARE_NAME
        self.SQUARE_ID = SQUARE_ID
        self.CURRENT_PIECE = BOARD.piece_at(chess.parse_square(self.SQUARE_NAME))


    def update_square():
        self.CURRENT_PIECE = BOARD.piece_at(chess.parse_square(self.SQUARE_NAME))



    def print_debug_data(self):
        print()
        print("***************************************************")
        print()
        print(f"I2C_ADDRESS (in hex):    {hex(self.I2C_ADDRESS)}")
        print(f"SQUARE_NAME:             {self.SQUARE_NAME}")
        print(f"SQUARE_ID:               {self.SQUARE_ID}")
        print(f"CURRENT_PIECE:           {self.CURRENT_PIECE}")
        print() 
        print("***************************************************")
        print()

    def print_board(self):        
        print(self.BOARD)

