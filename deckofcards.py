import random

class DeckOfCards:
    def __init__(self):
        self.deck = range(10)
    
    def draw(self):
        return random.choice(self.deck)