
import Functions.Create_Deck as make_deck
import Functions.Populate_Players as pop_players
import Functions.Deal_Hands as dealer

deck = make_deck.provide_deck()
player1, player2, player3, player4 = pop_players.create_players()
dealer.deal_hands(deck, player1, player2, player3, player4)

holder = player1.hand
for card in holder:
    print(card.suit)
    print(card.rank)
