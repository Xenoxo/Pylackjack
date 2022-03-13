
# tracks overall game rules like game over, player turn, score keeping
class GameController:

    def __init__(self, bankroll = 500):
        self.game_over = False
        self.player_base = ["player", "dealer"]

    def next_player(self):
        return self.player_base



##
# Below are temp things to verify functionalities while I build
##

face = GameController()

print(face.get_bankroll())

face1 = GameController(1000)

print(face1.get_bankroll())
