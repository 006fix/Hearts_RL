
import Functions.Create_Deck as make_deck
import Functions.Populate_Players as pop_players
import Functions.Deal_Hands as dealer

deck = make_deck.provide_deck()
player1, player2, player3, player4 = pop_players.create_players()
dealer.deal_hands(deck, player1, player2, player3, player4)

#now we update each players knowledge of the cards they hold
player1.initial_generate_data()
player1.first_populate_data()
player1.initial_other_knowledge()

player2.initial_generate_data()
player2.first_populate_data()
player2.initial_other_knowledge()

player3.initial_generate_data()
player3.first_populate_data()
player3.initial_other_knowledge()

player4.initial_generate_data()
player4.first_populate_data()
player4.initial_other_knowledge()

#below is a test sequence to confirm dealing worked
#holder = player1.hand
#for card in holder:
    #print(card.suit)
    #print(card.rank)
