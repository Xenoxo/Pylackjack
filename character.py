
from numpy import character


class Character:
    """Tracks the type of character, their hand and their money value (only when player)"""
    def __init__(self, type, bankroll = 500):
        self.hand = []
        self.type = type
        if (type == "player"):
            self.bankroll = bankroll
    
    def add_to_hand(self, card):
        self.hand.append(card)
    
    def character_type(self):
        return self.type


    def check_bankroll(self):
        try:
            return self.bankroll
        except AttributeError:
            print(f"WARNING: bankroll check for a {self.type} not implemented")

    def check_hand(self):
        #print(self.type)
        return self.hand
    
    def clearhand(self):
        self.hand = []
    
yo = Character("player", 6000)
yo1 = Character("dealer")

yo.add_to_hand("face")
print(yo.check_hand())
print(f"I am a {yo.character_type()}")
print(yo.check_bankroll())

print(yo1.check_bankroll())