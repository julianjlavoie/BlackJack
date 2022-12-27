import random


def addcard(who, score):
    card = int(random.choice(cards))

    def formatscore(_score):
        if card != 11 or (_score + card) <= 21:
            return card
        else:
            return 1

    if who == "player":
        playercards.append(str(formatscore(score)))
        return int(formatscore(score))
    elif who == "dealer":
        dealercards.append(str(formatscore(score)))
        return int(formatscore(score))


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealerrange = [15, 16, 17, 18]


playing = input("Do you want to play a hand of Blackjack? y/n ")
print("___________________________________________________________________")
while playing == "y":
    playercards = []
    dealercards = []
    playerscore = 0
    dealerscore = 0
    playerhold = False
    dealerhold = False

    # Game Setup

    playerscore += addcard("player", playerscore)
    playerscore += addcard("player", playerscore)
    dealerscore += addcard("dealer", dealerscore)
    dealerscore += addcard("dealer", dealerscore)

    # while neither score is 21 or over and at least one player is still hitting
    while playerscore < 21 and dealerscore < 21 and (playerhold is False or dealerhold is False):
        if playerhold is False:
            print(f"Your cards: {playercards}"), print(f"Dealers cards: {dealercards[0]}")
            response = input("Hit (H) or Stay (S)")
            print("    ___________________________________")
            if response == "H":
                playerscore += addcard("player", playerscore)
                if dealerscore < random.choice(dealerrange):
                    dealerscore += addcard("dealer", dealerscore)
                else:
                    dealerhold = True
            else:
                playerhold = True
        # If player holds, is dealer still hitting?
        else:
            if dealerhold is False and dealerscore < random.choice(dealerrange):
                dealerscore += addcard("dealer", dealerscore)
            else:
                dealerhold = True
    else:
        print(f"Your score: {playerscore}            Your Cards: {playercards}\n"
              f"Dealer score: {dealerscore}          Dealers Cards: {dealercards}")
        if dealerscore < playerscore <= 21 or dealerscore > 21 >= playerscore:
            print("\n            You are the Winner!")
            print("___________________________________________________________________")
        elif playerscore < dealerscore <= 21 or playerscore > 21 >= dealerscore:
            print("Dealer is the Winner. Better luck next time.")
            print("___________________________________________________________________")
    playing = input("Do you want to play again? y/n ")
    print("___________________________________________________________________")
