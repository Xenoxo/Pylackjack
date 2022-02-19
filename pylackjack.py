from deckofcards import DeckOfCards

the_deck = DeckOfCards()
print(f"count is {the_deck.count()}")
print(the_deck.draw())

# def func(x):
#     return x*2

# decklist = [func(x) for x in range(1,53)]

# print(decklist)           

# print("\nWelcome to the Blackjack game!")
# gamestart = input("\nDo you want to play? (y/n?) ")
# if gamestart == "y":
#     the_deck = DeckOfCards()
#     #print("let's pretend you have some cards")
#     player_choice = input("\nThere is a deck of cards in front of you, you can \"draw\" to get a card or anything else to exit the game.")
#     while player_choice == "draw":
#         card = the_deck.draw()
#         print(f"You drew a {card}!\n")
#         player_choice = input("What next?")
#     print("Thanks for playing!")
# else:
#     print("Cya Space Cowboy")

