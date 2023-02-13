

import Functions.Create_Deck as make_deck
import Functions.Deal_Hands as dealer

def game_start_func_sequence(player1, player2, player3, player4):
    deck = make_deck.provide_deck()
    dealer.deal_hands(deck, player1, player2, player3, player4)

    # now we update each players knowledge of the cards they hold
    player1.initial_generate_data()
    player1.first_populate_data()
    player1.initial_other_knowledge()
    player1.first_to_play()
    player1.update_alt_player_card_suits()
    player1.reset_players_left_to_play()
    # only enable if you need to test first turn no dump mechanics
    # player1.testing_noclubs()

    player2.initial_generate_data()
    player2.first_populate_data()
    player2.initial_other_knowledge()
    player2.first_to_play()
    player2.update_alt_player_card_suits()
    player2.reset_players_left_to_play()

    player3.initial_generate_data()
    player3.first_populate_data()
    player3.initial_other_knowledge()
    player3.first_to_play()
    player3.update_alt_player_card_suits()
    player3.reset_players_left_to_play()

    player4.initial_generate_data()
    player4.first_populate_data()
    player4.initial_other_knowledge()
    player4.first_to_play()
    player4.update_alt_player_card_suits()
    player4.reset_players_left_to_play()
