import Classes.Cards as card_class
import random

def provide_deck():

    suits = ['Heart', 'Club', 'Spade', 'Diamond']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []

    for i in suits:
        for j in ranks:
            hold_card = card_class.Card(i, j)
            deck.append(hold_card)

    random.shuffle(deck)

    return deck

