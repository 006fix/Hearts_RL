
played_cards = []
score_dict = {'player1': 0, 'player2': 0, 'player3': 0, 'player4': 0}
first_hand = 1
play_order = ['player1', 'player2', 'player3', 'player4', 'player1', 'player2', 'player3', 'player4']

#add a function here to calculate final score later

def calculate_score(play_dict, start_suit):
    ref_dict = {'curr_winner': 0}
    top_rank = 0
    points_for_hand = 0

    #identify winner
    for key in play_dict:
        if play_dict[key].suit == start_suit:
            if play_dict[key].rank > top_rank:
                top_rank = play_dict[key].rank
                ref_dict['curr_winner'] = key

    #identify points in hand
    for key in play_dict:
        if play_dict[key].suit == 'Heart':
            points_for_hand += 1
        if play_dict[key].suit == 'Spade':
            if play_dict[key].rank == 12:
                points_for_hand += 13

    holdval = score_dict[ref_dict['curr_winner'].name]
    holdval += points_for_hand
    score_dict[ref_dict['curr_winner']] = holdval

    winner = ref_dict['curr_winner']

    return winner