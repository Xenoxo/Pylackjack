from tabnanny import check
from matplotlib.pyplot import draw
from numpy import empty
from gamecontroller import GameController
from deckofcards import DeckOfCards

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
    reset()
    
    """MAIN GAME WHILE LOOP"""    
    while (player_choice != "quit" and gc.game_over == False):
        while len(dealer_hand) < 2:
            draw_card_action("PLAYER")
            draw_card_action("DEALER")       

        summarize_hand("DEALER") #summarize DEALER's hand
        
        check_current_hand("DEALER", dealer_card_value_sum, True) #check dealer for a Blackjack 
        check_current_hand("PLAYER", player_card_value_sum, True) #check player Blackjack
        
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
                check_current_hand("PLAYER", player_card_value_sum)
  
        summarize_hand('DEALER', True)
        #Deal remaining cards for DEALER
        while dealer_card_value_sum < 17 and gc.game_over == False:
            draw_card_action("DEALER")
            check_current_hand("DEALER", dealer_card_value_sum)
        
        #Resolve player and dealer hand
        if dealer_card_value_sum <= 21 and gc.game_over == False:
            summarize_hand("DEALER", True) #summarize DEALER hands
            print("\n\n=== FINAL RESULT === \n")
            if dealer_card_value_sum > player_card_value_sum:
                print(f"\nYour {player_card_value_sum} is less than the DEALER's {dealer_card_value_sum}, you lose.")
            elif dealer_card_value_sum == player_card_value_sum:
                print(f"\nYour {player_card_value_sum} is the same as the DEALER's {dealer_card_value_sum}, a PUSH!")     
            else:
                print(f"\nYour {player_card_value_sum} is greater than the DEALER's {dealer_card_value_sum}, you WIN!")
            
        player_choice = input("\nDo you want to play again? \"yes\" or \"no\"? ")
        if player_choice == "no":
            print("\n\n\nThanks for playing!!!\n\n\n")
            break
        reset()
        the_deck.shuffle()
    
def check_current_hand(character, hand_value, firsttime = False):
    """check for blackjack or busts"""
    if hand_value > 21 or hand_value == 21 and firsttime == True:
        global player_card_value_sum, dealer_card_value_sum
        actor = ""
        result = ""
        temp_card_sum = 0
        if character == "PLAYER":
            actor = "You have"
            temp_card_sum = player_card_value_sum
        elif character == "DEALER":
            actor = "Dealer has"
            temp_card_sum = dealer_card_value_sum
        if hand_value == 21:
            result = ", a Blackjack!"
        elif hand_value > 21:
            result = ", a BUST!"
        else:
            print(f"check_current_hand() method error: hand_value {hand_value} and firsttime is {firsttime}")
        print(f"\n{actor} a total of {temp_card_sum}{result}")
        gc.game_over = True


def draw_card_action(character):
    global the_deck, player_hand, player_card_value_sum, dealer_hand, dealer_card_value_sum
    actor = ""
    temp_hand = []
    drawn_card = the_deck.draw()
    temp_card_value = drawn_card['value']
    temp_card_name = drawn_card['name']
    if character == "PLAYER":
        actor = "You"
        temp_hand += player_hand
        player_card_value_sum += temp_card_value
        player_hand.append(drawn_card)
    elif character == "DEALER":
        if len(dealer_hand) == 0:
            temp_card_name = "facedown card"     
        actor = "Dealer"
        temp_hand = dealer_hand
        dealer_card_value_sum += temp_card_value
        dealer_hand.append(drawn_card)
    print(f"\n{actor} drew a {temp_card_name}.")


def summarize_hand(character, reveal = False):
    global player_hand, dealer_hand, player_card_value_sum, dealer_card_value_sum
    message = ""
    temp_hand = []
    temp_hand_sum_value = 0
    if character == "PLAYER":
        temp_hand = player_hand
        temp_hand_sum_value = player_card_value_sum
        message = f"\nYour hand totals {temp_hand_sum_value} with: "
    elif character == "DEALER":
        temp_hand = dealer_hand
        if reveal == False:
            #print(dealer_hand[0].value)
            fd_card = dealer_hand[0]
            #print(fd_card)
            temp_hand_sum_value = dealer_card_value_sum - dealer_hand[0]['value']
            message = f"\nThe Dealer\'s hand is showing {temp_hand_sum_value} with: "
        else:
            message = f"\nThe Dealer\'s hand totals {dealer_card_value_sum} with: "
    # summarizes the hand for corresponding actor
    print(message) 
    for card in temp_hand:
        if character == "DEALER" and reveal == False:
            print(f"|X|", end="  ")
            reveal = True
        else:
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
    gc.game_over = False


if __name__ == '__main__':
    main()