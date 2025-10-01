class Board:
    def __init__(self):
        self.size = 5
        self.reset()
    
    def reset(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.moves_count = 0  
    
    def display(self):
        print("\n    1   2   3   4   5")
        print("  +---+---+---+---+---+")
        
        for i in range(5):
            row = self.board[i]
            print(f"{i+1} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |")
            if i < 4:
                print("  +---+---+---+---+---+")
            else:
                print("  +---+---+---+---+---+")
        print()
    
    def make_move(self, row, col, symbol):
        if row < 0 or row > 4 or col < 0 or col > 4:
            print("Invalid move! Row and column must be between 1 and 5.")
            return False
        
        if self.board[row][col] != ' ':
            print("That position is already taken! Choose another.")
            return False
        
        self.board[row][col] = symbol
        self.moves_count += 1  
        return True
    
    def check_winner(self, symbol):
    
        for row in range(5):
            for col in range(1):
                if (self.board[row][col] == symbol and 
                    self.board[row][col+1] == symbol and 
                    self.board[row][col+2] == symbol and 
                    self.board[row][col+3] == symbol and 
                    self.board[row][col+4] == symbol):
                    return True
        
      
        for col in range(5):
            for row in range(1):
                if (self.board[row][col] == symbol and 
                    self.board[row+1][col] == symbol and 
                    self.board[row+2][col] == symbol and 
                    self.board[row+3][col] == symbol and 
                    self.board[row+4][col] == symbol):
                    return True
        
        for row in range(1):
            for col in range(1):
                if (self.board[row][col] == symbol and 
                    self.board[row+1][col+1] == symbol and 
                    self.board[row+2][col+2] == symbol and 
                    self.board[row+3][col+3] == symbol and 
                    self.board[row+4][col+4] == symbol):
                    return True
        
        
        for row in range(1):
            for col in range(4, 5):
                if (self.board[row][col] == symbol and 
                    self.board[row+1][col-1] == symbol and 
                    self.board[row+2][col-2] == symbol and 
                    self.board[row+3][col-3] == symbol and 
                    self.board[row+4][col-4] == symbol):
                    return True
        
        return False
    
    def is_full(self):
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == ' ':
                    return False
        return True
