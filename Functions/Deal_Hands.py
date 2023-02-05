def deal_hands(deck, player1, player2, player3, player4):

    for i in range(1, len(deck)+1):
        if i%4 == 1:
            player1.hand.append(deck[i-1])
        elif i%4 == 2:
            player2.hand.append(deck[i-1])
        elif i%4 == 3:
            player3.hand.append(deck[i-1])
        elif i%4 == 0:
            player4.hand.append(deck[i-1])
        else:
            raise ValueError("Unknown error occured during dealing, please investigate")


