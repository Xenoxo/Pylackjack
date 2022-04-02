"""

while the game is going (player has money, player hasn't quit, enough cards are left in deck[>12 b/c 12 is all A's, 2's and 3's])

    cards are dealt to dealer and player in sequence (player, dealer) until both participants have 2 cards
    if dealer has 21, round over else....
    while player !stayed & <= 21
        Player can hit
    Dealer reveals card
    While dealer card < 17 
        dealer hit
    compare cards
    w/l/p => update counters scores and money

"""


"""
    while player_choice != "q":

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


