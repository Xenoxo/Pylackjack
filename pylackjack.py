import gamecontroller as gc 
from gamecontroller import GameController
from deckofcards import DeckOfCards
#from test_deck_of_cards import TestDeckOfCards

def main():
    gc = GameController()
    the_deck = DeckOfCards()
    print(gc.bankroll)

    player_hand = []
    dealer_hand = []
    player_card_value_sum = 0
    dealer_card_value_sum = 0
    player_choice = ""
    sum = 0

    print("\nWelcome to the Blackjack game!")

    while (player_choice != "q" and gc.game_over == False):

   ####### DEAL CARDS
        while len(dealer_hand) < 2:

        #deal to player
            player_card = the_deck.draw()
            print(f"\nYou drew a {player_card['name']}!")
            player_hand.append(player_card)
            player_card_value_sum += player_card['value']            

        #deal dealer
            dealer_card = the_deck.draw()
            print(f"\nDealer drew a {dealer_card['name']}!")
            dealer_hand.append(dealer_card)
            dealer_card_value_sum += dealer_card['value']            
        
        #summarize DEALER hands

        print("\nThe DEALER is showing: ")
        for card in dealer_hand:
            print(f"{card['name']}", end="  ")
        print(f"\nDEALER hand totals: {dealer_card_value_sum}")            
        
        #check dealer Blackjack
        if dealer_card_value_sum == 21:
            print(f"Dealer has a total of {dealer_card_value_sum}, a BLACKJACK! Tough luck!")
            break

        #summarize player hand
        print("\n\nYour hand is: ")
        for card in player_hand:
            print(f"{card['name']}", end="  ")
        print(f"\nYour hand totals: {player_card_value_sum}")
        
        #check player
        if player_card_value_sum == 21:
            print(f"You got a blackjack with {player_card_value_sum}!")
            break


        #player choice after cards are dealt

        player_choice = input("\nDo you want to \"hit\" or \"stay\"? ")
        
        while player_choice != "stay" and player_card_value_sum < 21:
            
            player_card = the_deck.draw()
            print(f"\nYou drew a {player_card['name']}!")
            player_hand.append(player_card)
            player_card_value_sum += player_card['value']            

          #summarize player hand
            print("Your hand is: ")
            for card in player_hand:
                print(f"{card['name']}", end="  ")
            print(f"\nYour hand totals: {player_card_value_sum}")

            if player_card_value_sum < 21:
                player_choice = input("\nHit or Stay? ")

        if player_card_value_sum > 21:
            print("\nYOU BUST! ")
            break
        
        while dealer_card_value_sum < 17:
        #deal dealer
            dealer_card = the_deck.draw()
            print(f"\nDealer drew a {dealer_card['name']}!")
            dealer_hand.append(dealer_card)
            dealer_card_value_sum += dealer_card['value']            
        
        if dealer_card_value_sum > 21:
            print("\nDEALER BUSTS! YOU WIN!!!!! ")
            break


        #summarize DEALER hands

        print("\nThe DEALER is showing: ")
        for card in dealer_hand:
            print(f"{card['name']}", end="  ")
        print(f"\nDEALER hand totals: {dealer_card_value_sum}")            
        
        if dealer_card_value_sum > player_card_value_sum:
            print(f"\nYour {player_card_value_sum} is less than the DEALER's {dealer_card_value_sum}, you lose")
        elif dealer_card_value_sum == player_card_value_sum:
            print(f"\nYour {player_card_value_sum} is the same as the DEALER's {dealer_card_value_sum}, a PUSH!")     
        else:
            print(f"\nYour {player_card_value_sum} is greater than the DEALER's {dealer_card_value_sum}, you WIN!")                       
        
        
        break
"""
        # temp function to check deck size
        if player_choice == "count":
            print(the_deck.count())    

        card = the_deck.draw() # draws a card

        if card != False: # meaning there are still cards left in the deck
            player_hand.append(card)
            print(f"\nYou drew a {card}!")
        
        if player_hand == False:
            print("\nYour hand is currently empty")
        else:
            print(f"Your had is: ")
            for card in player_hand:
                print(f"{card}", end="  ")
        player_choice = input("\nagain? ")
"""

if __name__ == '__main__':
    main()