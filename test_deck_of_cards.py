import unittest
from deckofcards import DeckOfCards

class TestDeckOfCards(unittest.TestCase):
    """Tests for the class DeckOfCards"""
    def setUp(self):
        """Creates a deck of cards to be tested"""
        self.test_deck = DeckOfCards()
    
    def test_draw_a_card(self):
        """test drawing a single card removes it from the deck"""
        self.card = self.test_deck.draw()
        self.assertTrue(self.test_deck.count() == 51)

    def test_draw_till_empty(self):
        """Test draw function when deck is empty"""
        while self.test_deck.count() > 0:
            self.test_deck.draw()
        self.assertTrue(self.test_deck.count() == 0)

    def test_count_function(self):
        """Tests count() method"""
        self.assertEqual(self.test_deck.count(), 52)

if __name__ == '__main__':
    unittest.main()