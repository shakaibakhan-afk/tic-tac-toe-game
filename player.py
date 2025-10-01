class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def get_move(self):
        try:
            row = int(input(f"{self.name}, enter row (1-5): ")) - 1
            col = int(input(f"{self.name}, enter column (1-5): ")) - 1
            return row, col
        except:
            print("Please enter valid numbers!")
            return self.get_move()