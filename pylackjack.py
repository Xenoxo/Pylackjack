from matplotlib.pyplot import draw
from numpy import empty
import gamecontroller as gc 
from gamecontroller import GameController
from deckofcards import DeckOfCards
#from test_deck_of_cards import TestDeckOfCards

balskdfjsadl = "musky"

player_hand = []
dealer_hand = []
player_card_value_sum = 0
dealer_card_value_sum = 0
player_choice = ""
the_deck = DeckOfCards()    

def main():
    global player_hand, player_choice
    global dealer_hand
    global player_card_value_sum
    global dealer_card_value_sum
    global the_deck

    gc = GameController()



    print("\nWelcome to the Blackjack game!\n")
    
    """MAIN GAME WHILE LOOP"""    
    while (player_choice != "quit" and gc.game_over == False):

        ### DEALS OUT CARDS FOR DEALER AND PLAYER
        while len(dealer_hand) < 2:
            draw_card_action("PLAYER")
            draw_card_action("DEALER")       
        
        summarize_hand("DEALER") #summarize DEALER's hand
        
        #check dealer Blackjack
        if dealer_card_value_sum == 21:
            print(f"Dealer has a total of {dealer_card_value_sum}, a BLACKJACK! Tough luck!")
            break

        #summarize PLAYER's hand
        summarize_hand("PLAYER")
        
        #check player Blackjack
        if player_card_value_sum == 21:
            print(f"You got a blackjack with {player_card_value_sum}!")
            break


        #PLAYER choice after cards are dealt
        player_choice = input("\nDo you want to \"hit\" or \"stay\"? ")
        while player_choice != "stay" and player_card_value_sum < 21:
            
            player_card = the_deck.draw()
            print(f"\nYou drew a {player_card['name']}!")
            player_hand.append(player_card)
            player_card_value_sum += player_card['value']                      
            
            summarize_hand("PLAYER") #summarize player hand
            
        #PLAYER choice
            if player_card_value_sum < 21:
                player_choice = input("\nHit or Stay? ")
        
        if player_card_value_sum > 21:
            print("\nYOU BUST! ")
            break
  
        #Deal rest for DEALER
        while dealer_card_value_sum < 17:
            dealer_card = the_deck.draw()
            print(f"\nDealer drew a {dealer_card['name']}!")
            dealer_hand.append(dealer_card)
            dealer_card_value_sum += dealer_card['value']            
        
        #Check dealer bust
        if dealer_card_value_sum <= 21:
            summarize_hand("DEALER") #summarize DEALER hands
     
            if dealer_card_value_sum > player_card_value_sum:
                print(f"\nYour {player_card_value_sum} is less than the DEALER's {dealer_card_value_sum}, you lose")
            elif dealer_card_value_sum == player_card_value_sum:
                print(f"\nYour {player_card_value_sum} is the same as the DEALER's {dealer_card_value_sum}, a PUSH!")     
            else:
                print(f"\nYour {player_card_value_sum} is greater than the DEALER's {dealer_card_value_sum}, you WIN!")                       
        elif dealer_card_value_sum > 21: 
            print("\nDEALER BUSTS! YOU WIN!!!!! ")
        else:
            print(f"THIS IS WEIRD!!!! The dealer hand value is {dealer_card_value_sum}" )
            
       
      #  print(f"{the_deck.count()} CARDS NOW!!!!!!!")

        player_choice = input("\nDo you want to play again? \"yes\" or \"no\"? ")
        if player_choice == "no":
            print("\n\n\nThanks for playing!!!\n\n\n")
            break
        the_deck.shuffle()
        player_hand = []
        dealer_hand = []
        player_card_value_sum = 0
        dealer_card_value_sum = 0

def draw_card_action(character):
    global the_deck, player_hand, player_card_value_sum, dealer_hand, dealer_card_value_sum
    actor = ""
    temp_hand = []
    drawn_card = the_deck.draw()
    temp_card_sum = drawn_card['value']
    if character == "PLAYER":
        actor = "You"
        temp_hand += player_hand
        player_card_value_sum += temp_card_sum
        player_hand.append(drawn_card)
    elif character == "DEALER":
        actor = "Dealer"
        temp_hand = dealer_hand
        dealer_card_value_sum += temp_card_sum
        dealer_hand.append(drawn_card)
    print(f"\n{actor} drew a {drawn_card['name']}.")


def summarize_hand(character):
    global player_hand, dealer_hand, player_card_value_sum, dealer_card_value_sum
    actor = ""
    temp_hand = []
    temp_hand_sum_value = 0
    if character == "PLAYER":
        actor = "Your"
        temp_hand = player_hand
        temp_hand_sum_value = player_card_value_sum
    elif character == "DEALER":
        actor = "Dealer\'s"
        temp_hand = dealer_hand
        temp_hand_sum_value = dealer_card_value_sum
    
    # summarizes the hand for corresponding actor
    print(f"\n\n{actor} hand is: ") 
    for card in temp_hand:
        print(f"{card['name']}", end="  ")
    print(f"\n{actor} hand totals: {temp_hand_sum_value}")

def reset():
    global player_hand, player_choice
    global dealer_hand
    global player_card_value_sum
    global dealer_card_value_sum
    global the_deck
    global balskdfjsadl
        
    player_hand = []
    dealer_hand = []
    player_card_value_sum = 0
    dealer_card_value_sum = 0
    the_deck = DeckOfCards()    
    player_choice = ""


if __name__ == '__main__':
    main()