from board import Board
from player import Player
from save_game import GameSaveManager

class TicTacToeGame:
    def __init__(self):
        """Initialize game with board, players, and save manager"""
        self.board = Board()
        self.players = []
        self.current_player_index = 0
        self.game_status = "ongoing"
        self.save_manager = GameSaveManager()
    
    def setup_players(self):
        """Get player names and create player objects"""
        print("=== 5x5 Tic Tac Toe Game ===")
        name1 = input("Enter name for Player 1 (X): ") or "Player 1"
        name2 = input("Enter name for Player 2 (O): ") or "Player 2"
        
        self.players = [
            Player(name1, 'X'),
            Player(name2, 'O')
        ]
        
        print(f"Game started: {name1} (X) vs {name2} (O)")
    
    def setup_players_from_save(self, saved_players):
        """Create players from saved game data"""
        self.players = [
            Player(saved_players[0]['name'], saved_players[0]['symbol']),
            Player(saved_players[1]['name'], saved_players[1]['symbol'])
        ]
        print(f"Players loaded: {self.players[0].name} (X) vs {self.players[1].name} (O)")
    
    def get_current_player(self):
        """Return the player whose turn it is"""
        return self.players[self.current_player_index]
    
    def switch_player(self):
        """Switch turn to the other player"""
        self.current_player_index = 1 if self.current_player_index == 0 else 0
    
    def check_winner(self):
        """Check if current player won or game is draw"""
        current_player = self.get_current_player()
        
        # Check if current player won (jo move kiya usne)
        if self.board.check_winner(current_player.symbol):
            print(f"\nCongratulations! {current_player.name} wins!")
            self.game_status = "finished"
            return True
        
        # Check if board full (draw)
        if self.board.is_full():
            print("\nIt's a draw!")
            self.game_status = "draw"
            return True
        
        return False
    
    def play_turn(self):
        """Play one turn - get move, update board, check winner"""
        player = self.get_current_player()
        print(f"\n{player.name}'s turn ({player.symbol})")
        self.board.display()
        
        # Get valid move from player with restart option
        while True:
            try:
                # Get row input with restart option
                row_input = input(f"{player.name}, enter row (1-5): ").strip().upper()
                if row_input == 'R':
                    confirm = input("Are you sure you want to restart? (y/n): ").lower()
                    if confirm == 'y':
                        print("\n🔄 Game restarting with same players...")
                        self.new_game()
                        return True
                    else:
                        continue
                
                row = int(row_input) - 1
                
                # Get column input with restart option
                col_input = input(f"{player.name}, enter column (1-5): ").strip().upper()
                if col_input == 'R':
                    confirm = input("Are you sure you want to restart? (y/n): ").lower()
                    if confirm == 'y':
                        print("\n🔄 Game restarting with same players...")
                        self.new_game()
                        return True
                    else:
                        continue
                
                col = int(col_input) - 1
                
                if self.board.make_move(row, col, player.symbol):
                    break
                else:
                    print("Invalid move! Try again.")
                    
            except ValueError:
                print(" Please enter valid numbers (1-5) or 'R' to restart!")
        
        # Check if game over after move
        if self.check_winner():
            # Game khatam hone par final state save karo
            self.save_manager.save_game(
                self.board.board,
                player.symbol,  
                self.game_status, 
                self.players
            )
            print("Final game state saved!")
            self.board.display()
            return False
        
        # Switch to next player
        self.switch_player()
        
        # Save ongoing game
        self.save_manager.save_game(
            self.board.board,
            self.get_current_player().symbol,  
            self.game_status, 
            self.players
        )
        print("Game saved!")
        
        return True
    
    def load_game(self):
        """Load saved game from file and restore state"""
        save_data = self.save_manager.load_game()
        if save_data is None:
            print("No saved game found!")
            return False
        
        self.board.board = save_data['board']
        
        if 'players' in save_data:
            self.setup_players_from_save(save_data['players'])
        else:
            self.setup_players()
        
        current_player_symbol = save_data['current_player']
        for i, player in enumerate(self.players):
            if player.symbol == current_player_symbol:
                self.current_player_index = i
                break
        
        self.game_status = save_data['game_status']
        
        print(f"Game loaded successfully! Status: {self.game_status}")
        return True
    
    def show_menu(self):
        """Display main menu options"""
        print("\n=== Main Menu ===")
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")
    
    def new_game(self):
        """Reset board and start new game"""
        self.board.reset()
        self.game_status = "ongoing"
        self.current_player_index = 0
        
        if not self.players:
            self.setup_players()
        
        print("\nStarting new game!")
        self.play_game()
    
    def play_game(self):
        """Main game loop - keep playing turns until game ends"""
        while self.game_status == "ongoing":
            if not self.play_turn():
                break
        
        # Game khatam hone par status show karo
        if self.game_status == "finished":
            print("\n🎉 Game finished with a winner! 🎉")
        elif self.game_status == "draw":
            print("\n🤝 Game ended in a draw! 🤝")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again == 'y':
            self.new_game()
        else:
            print("Thanks for playing!")
    
    def run(self):
        """Main program loop - show menu and handle user choices"""
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                self.new_game()
            elif choice == '2':
                if self.load_game():
                    self.play_game()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    """Start the game when file is run directly"""
    game = TicTacToeGame()
    game.run()