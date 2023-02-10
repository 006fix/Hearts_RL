import Game_Space.Playing_Table as game_data
import Functions.player_actions as player_actions

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

    play_list = {'play_order': 0}
    hold_str = "play_list['play_order'] = ["
    for i in play_order:
        hold_str += i
        hold_str += ", "
    hold_str = hold_str[:-2]
    hold_str += "]"

    #this gives us a sequential list of order of play
    print(hold_str)
    exec(hold_str)

    #making a variable to hold current_player
    cur_player_dict = {'cur_player': 0}

    if first_turn == 1:
        #run the function to play a card, but simply provide the 2 of clubs for first player
        #then for the remainder, play as normal
        print(f"First player is {first_player}")
        exec(f"{first_player}.play_card('Club',2)")
        #here we need a function that updates each players knowledge
        player_actions.update_player_knowledge(player1, player2, player3, player4, first_player, 'Club', 2, 'Club', True, False, game_data.score_dict)
        for i in range(len(play_list['play_order'])):
            if i == 0:
                pass
            else:
                exec(f"cur_player_dict['cur_player'] = play_list['play_order'][{i}]")
                print(cur_player_dict)
                valid_options = player_actions.identify_card_to_player(cur_player_dict['cur_player'], 'Club', first_turn)
                print(f"The valid options for {cur_player_dict['cur_player'].name} are:")
                for card in valid_options:
                    print(f"{card.suit}-{card.rank}")

    else:
        #play as normal
        pass



