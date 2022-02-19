from deckofcards import DeckOfCards

print("\nWelcome to the Blackjack game!")

gamestart = input("\nDo you want to play? (y/n?) ")

if gamestart == "y":
    the_deck = DeckOfCards()
    player_choice = input("\nThere is a deck of cards in front of you, you can type \"draw\" \n(any other input exits the game): ")
    while player_choice == "draw":
        card = the_deck.draw()
        print(f"You drew a {card}!\n")
        player_choice = input("What next? ")
    print("Thanks for playing!")
else:
    print("Cya Space Cowboy")

# the_deck = DeckOfCards() 
# print(f"count is {the_deck.count()}")
# print(the_deck.draw())