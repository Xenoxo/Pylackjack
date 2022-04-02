import random

class DeckOfCards:
    def __init__(self):
        self.deck = [self.func(x % 13 , x // 13) for x in range(52)]
    
    def draw(self):
        """by default returns the name of the card dictionary"""
        if self.count() > 0:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card
        else:
            print("\nTHERE ARE NO MORE CARDS LEFT IN THE DECK\n")
            return False
    
    #def card_details(self):


    def count(self):
        """
        Returns the number of cards left in the deck
        """
        return len(self.deck)
    
    def func(self, value_num, suit_num):
        """
        Generates each card for the deck
        value_num is 1 - 12, suit_num is 1 - 4: these are used to build every card
        """
        card_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
        card_suit = ["\u2660", "\u2665", "\u2666", "\u2663"]
        card = {
                "id" : value_num,
                "name" : f"|{card_rank[value_num]} {card_suit[suit_num]}|",
                "rank" : card_rank[value_num],
                "value" : card_value[value_num],
                "suit" : card_suit[suit_num],
            }
        return card