
# tracks overall game rules like game over, player turn, score keeping
class GameController:

    def __init__(self, bankroll = 500):
        self.game_over = False
        self.bankroll = bankroll
            

    def moneyCount(self):
        return self.bankroll



##
# Below are temp things to verify functionalities while I build
##
face = GameController()

print(face.moneyCount())

face1 = GameController(1000)

print(face1.moneyCount())
