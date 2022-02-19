import random

class DeckOfCards:
    def __init__(self):
        """generates the cards for the deck"""
        def func(value_num, suit_num): #cardvaule is 1 - 12, suit is 1 - 4
            card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            card_suit = ["S", "H", "D", "C"]
            card = {
                    "id" : value_num,
                    "name" : f"{card_value[value_num]} {card_suit[suit_num]}",
                    "value" : card_value[value_num],
                    "suit" : card_suit[suit_num],
                }
            return card
        self.deck = [func(x % 13 , x // 13) for x in range(52)]
    
    def draw(self):
        """by default returns the name of the card dictionary"""
        return random.choice(self.deck)["name"]

    def count(self):
        return len(self.deck)