from matplotlib.pyplot import draw
from numpy import empty
#import gamecontroller as gc 
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
gc = GameController()

def main():
    global player_hand, player_choice, dealer_hand, player_card_value_sum, dealer_card_value_sum, the_deck, gc

    print("\nWelcome to the Blackjack game!\n")
    
    """MAIN GAME WHILE LOOP"""    
    while (player_choice != "quit" and gc.game_over == False):
        reset()
        while len(dealer_hand) < 2:
            draw_card_action("PLAYER")
            draw_card_action("DEALER")       

        summarize_hand("DEALER") #summarize DEALER's hand
        
        check_current_hand("DEALER") #check dealer for a Blackjack 
        check_current_hand("PLAYER") #check player Blackjack
        
        """PLAYER choice loop after cards are dealt and no natural Blackjacks"""
        if gc.game_over == False:
            summarize_hand("PLAYER") #summarize PLAYER's hand
            player_choice = input("\nDo you want to \"hit\" or \"stay\"? ")
            print("\n")
            while player_choice != "stay" and player_card_value_sum < 21 and gc.game_over == False:
                draw_card_action("PLAYER")           
                summarize_hand("PLAYER") #summarize player hand
                if player_card_value_sum < 21: #player choice
                    player_choice = input("\nHit or Stay? ")
                elif player_card_value_sum > 21:
                    print(f"\nYOU BUST with a {player_card_value_sum}! ")
                    gc.game_over = True
  
        #Deal remaining cards for DEALER
        while dealer_card_value_sum < 17 and gc.game_over == False:
            draw_card_action("DEALER")        
        
        #Resolve player and dealer hand
        if dealer_card_value_sum <= 21 and gc.game_over == False:
            summarize_hand("DEALER") #summarize DEALER hands
            if dealer_card_value_sum > player_card_value_sum:
                print(f"\nYour {player_card_value_sum} is less than the DEALER's {dealer_card_value_sum}, you lose.")
            elif dealer_card_value_sum == player_card_value_sum:
                print(f"\nYour {player_card_value_sum} is the same as the DEALER's {dealer_card_value_sum}, a PUSH!")     
            else:
                print(f"\nYour {player_card_value_sum} is greater than the DEALER's {dealer_card_value_sum}, you WIN!")                       
        elif dealer_card_value_sum > 21 and gc.game_over == False: 
            print("\nDEALER BUSTS! YOU WIN!!!!! ")
        elif gc.game_over == False:
            print(f"SEEING THIS WOULD BE WEIRD! The dealer hand value is {dealer_card_value_sum}" )
            
        player_choice = input("\nDo you want to play again? \"yes\" or \"no\"? ")
        if player_choice == "no":
            print("\n\n\nThanks for playing!!!\n\n\n")
            break

        the_deck.shuffle()
    
def check_current_hand(character):
    global player_card_value_sum, dealer_card_value_sum
    actor = ""
    temp_card_sum = 0
    if character == "PLAYER":
        actor = "You have"
        temp_card_sum = player_card_value_sum
    elif character == "DEALER":
        actor = "Dealer has"
        temp_card_sum = dealer_card_value_sum
    if temp_card_sum == 21:
        print(f"{actor} a total of {temp_card_sum}, a BLACKJACK!")
        gc.game_over = True


def draw_card_action(character):
    global the_deck, player_hand, player_card_value_sum, dealer_hand, dealer_card_value_sum
    actor = ""
    temp_hand = []
    drawn_card = the_deck.draw()
    temp_card_value = drawn_card['value']
    temp_card_sum = 0
    if character == "PLAYER":
        actor = "You"
        temp_hand += player_hand
        player_card_value_sum += temp_card_value
        #temp_card_sum = player_card_value_sum
        player_hand.append(drawn_card)
    elif character == "DEALER":
        actor = "Dealer"
        temp_hand = dealer_hand
        dealer_card_value_sum += temp_card_value
        #temp_card_sum = player_card_value_sum
        dealer_hand.append(drawn_card)
    print(f"{actor} drew a {drawn_card['name']}.")


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
    print(f"\n{actor} hand totals {temp_hand_sum_value} with: ") 
    for card in temp_hand:
        print(f"{card['name']}", end="  ")

def reset():
    global player_hand, player_choice
    global dealer_hand
    global player_card_value_sum
    global dealer_card_value_sum
    global the_deck
    global gc
        
    player_hand = []
    dealer_hand = []
    player_card_value_sum = 0
    dealer_card_value_sum = 0
    player_choice = ""
    the_deck = DeckOfCards()    
    gc = GameController()


if __name__ == '__main__':
    main()