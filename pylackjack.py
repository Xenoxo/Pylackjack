from calendar import TUESDAY
from deckofcards import DeckOfCards
#from test_deck_of_cards import TestDeckOfCards

def main():

    print("yoyo")

    print("\nWelcome to the Blackjack game!")

    #       BELOW CODE IS FOR PROPER GAME FORMAT
    # gamestart = input("\nDo you want to play? (y/n?) ")
    #
    # if gamestart == "y":
    #     the_deck = DeckOfCards()
    #     player_choice = input("\nThere is a deck of cards in front of you, you can type \"draw\" \n(any other input exits the game): ")
    #     while player_choice == "draw":
    #         card = the_deck.draw()
    #         print(f"You drew a {card}!\n")
    #         player_choice = input("What next? ")
    #     print("Thanks for playing!")
    # else:
    #     print("Cya Space Cowboy")


    player_hand = []
    player_choice = ""
    the_deck = DeckOfCards() 
    while player_choice != "q":

        if player_choice == "count":
            print(the_deck.count())    

        card = the_deck.draw()
        if card != False:
            player_hand.append(card)
            print(f"\nYou drew a {card}!")
        
        if player_hand == False:
            print("\nYour hand is currently empty")
        else:
            print(f"Your had is: ")
            for card in player_hand:
                print(f"{card}", end="  ")
        player_choice = input("\nagain? ")


    # print(f"count is {the_deck.count()}")
    # print(the_deck.draw())
if __name__ == '__main__':
    main()