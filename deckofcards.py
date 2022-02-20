import random

class DeckOfCards:
    def __init__(self):
        self.deck = [self.func(x % 13 , x // 13) for x in range(52)]
    
    def draw(self):
        """by default returns the name of the card dictionary"""
        if self.count() > 0:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card["name"]
        else:
            print("\nTHERE ARE NO MORE CARDS LEFT IN THE DECK\n")
            return False

    def count(self):
        return len(self.deck)

    
    def func(self, value_num, suit_num): #cardvaule is 1 - 12, suit is 1 - 4
        """generates each card for the deck"""
        card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_suit = ["S", "H", "D", "C"]
        card = {
                "id" : value_num,
                "name" : f"{card_value[value_num]}|{card_suit[suit_num]}",
                "value" : card_value[value_num],
                "suit" : card_suit[suit_num],
            }
        return card