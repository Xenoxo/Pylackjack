import random

class DeckOfCards:
    def __init__(self):
        def func(value_num, suit_num): #cardvaule is 1 - 12, suit is 1 - 4
            card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            card_suit = ["S", "H", "D", "C"]
            card = {
                    "id" : value_num,
                    "value" : card_value[value_num],
                    "suit" : card_suit[suit_num],
                }
            return card
            # f"{card_value[value_num]}, {card_suit[suit_num]}"
            if x % 4 == 1:
                return x*2
        #self.deck = [x for x in range(1,53)]
        self.deck = [func(x % 13 , x // 13) for x in range(52)]
        #print(self.deck)
        
        #self.deck = range(52)
    
    def draw(self):
        return random.choice(self.deck)

    def count(self):
        return len(self.deck)