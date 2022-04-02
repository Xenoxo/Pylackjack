
class GameController:
    """tracks overall game rules like game over, player turn, score keeping"""

    def __init__(self, bankroll = 500):
        self.game_over = False
        self.player_base = ["player", "dealer"]
        self.bankroll = bankroll

    def next_player(self):
        return self.player_base
    
    def next_phase(self):
        return True
    
    def hand_result(self, result):
        return result
    



##
# Below are temp things to verify functionalities while I build
##
