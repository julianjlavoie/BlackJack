import random

# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# ## There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.


# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
# instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11
# and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is
# over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the
# deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be
# repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards
# as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer
# and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the
# computer_score is over 21, then the computer loses. If none of the above, then the player with the highest
# score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new
# game of blackjack and show the logo from art.py.


def addcard(who):
    if who == "player":
        card = random.choice(cards)
        playercards.append(card)
        return int(card)
    elif who == "dealer":
        card = random.choice(cards)
        dealercards.append(card)
        return int(card)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealerrange = [15, 16, 17, 18]
playing = "y"
while playing == "y":
    playercards = []
    dealercards = []
    playerscore = 0
    dealerscore = 0
    playerhold = False
    dealerhold = False

    playing = input("Do you want to play a hand of Blackjack? y/n ")
    # Game Setup

    playerscore += addcard("player")
    playerscore += addcard("player")
    dealerscore += addcard("dealer")
    dealerscore += addcard("dealer")
    print(f"Your cards: {playercards}"), print(f"Dealers cards: {dealercards[0]}")

    # while neither score is 21 or over and at least one player is still hitting
    while playerscore < 21 and dealerscore < 21 and (playerhold is False or dealerhold is False):
        if playerhold is False:
            response = input("Hit (H) or Stay (S)")
            if response == "H":
                playerscore += addcard("player")
                if dealerscore < random.choice(dealerrange):
                    dealerscore += addcard("dealer")
                else:
                    dealerhold = True
            else:
                playerhold = True
        # If player holds, is dealer still hitting?
        else:
            if dealerhold is False and dealerscore < random.choice(dealerrange):
                dealerscore += addcard("dealer")
            else:
                dealerhold = True
    else:
        print(f"Your score: {playerscore}\nDealer score: {dealerscore}")

        if dealerscore < playerscore <= 21 or dealerscore > 21 >= playerscore:
            print("You are the Winner!")
        elif playerscore < dealerscore <= 21 or playerscore > 21 >= dealerscore:
            print("Dealer is the Winner. Better luck next time.")
