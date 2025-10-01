import json
import os

class GameSaveManager:
    def __init__(self):
        self.save_dir = "saves"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    def save_game(self, board, current_player, game_status, players):
        save_data = {
            'board': board,
            'current_player': current_player,
            'game_status': game_status,
            'players': [
                {'name': players[0].name, 'symbol': players[0].symbol},
                {'name': players[1].name, 'symbol': players[1].symbol}
            ]
        }
        
        filename = "current_game.json"
        filepath = os.path.join(self.save_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(save_data, f)
        
        return filename
    
    def load_game(self):
        filepath = os.path.join(self.save_dir, "current_game.json")
        
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r') as f:
            save_data = json.load(f)
        
        return save_data
    
    def delete_save(self):
        """
        
        """
        filepath = os.path.join(self.save_dir, "current_game.json")
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False