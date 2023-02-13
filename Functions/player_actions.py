
def update_player_knowledge(player1, player2, player3, player4, player_played, card_suit, card_rank, start_suit, followed_suit, hand_finished, score_dict):

    player1.update_knowledge(player_played, card_suit, card_rank, start_suit, followed_suit, hand_finished, score_dict)
    player2.update_knowledge(player_played, card_suit, card_rank, start_suit, followed_suit, hand_finished, score_dict)
    player3.update_knowledge(player_played, card_suit, card_rank, start_suit, followed_suit, hand_finished, score_dict)
    player4.update_knowledge(player_played, card_suit, card_rank, start_suit, followed_suit, hand_finished, score_dict)

def identify_card_to_player(player, start_suit, first_turn, broken):

    valid_options = player.identify_valid_cards(start_suit, first_turn, broken)

    return valid_options