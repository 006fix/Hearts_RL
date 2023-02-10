import Game_Space.Playing_Table as game_data

def play_hand(player1, player2, player3, player4, first_turn):

    first_player = ''

    if player1.first_to_play == 1:
        first_player = 'player1'
    elif player2.first_to_play == 1:
        first_player = 'player2'
    elif player3.first_to_play == 1:
        first_player = 'player3'
    elif player4.first_to_play == 1:
        first_player = 'player4'

    start_point = game_data.play_order.index(first_player)
    play_order = game_data.play_order[start_point:start_point+4]

    hold_str = "play_list = ["
    for i in play_order:
        hold_str += i
        hold_str += ", "
    hold_str = hold_str[:-2]
    hold_str += "]"

    #this gives us a sequential list of order of play
    exec(hold_str)

    if first_turn == 1:
        #run the function to play a card, but simply provide the 2 of clubs for first player
        #then for the remainder, play as normal
        print(f"First player is {first_player}")
        exec(f"{first_player}.play_card('Club',2)")
        #here we need a function that updates each players knowledge
        player1.update_knowledge(first_player, 'Club', 2, 'Club', True, False, game_data.score_dict)
        player2.update_knowledge(first_player, 'Club', 2, 'Club', True, False, game_data.score_dict)
        player3.update_knowledge(first_player, 'Club', 2, 'Club', True, False, game_data.score_dict)
        player4.update_knowledge(first_player, 'Club', 2, 'Club', True, False, game_data.score_dict)
    else:
        #play as normal
        pass



