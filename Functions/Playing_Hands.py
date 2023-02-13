import Game_Space.Playing_Table as game_data
import Functions.player_actions as player_actions

def play_hand(player1, player2, player3, player4, first_turn, broken, everbroken):

    #stores record of player and card played
    play_dict = {}
    #this variable holds the most recently played card
    selected_card_dict = {'recent_card': 0}

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
        exec(f"selected_card_dict['recent_card'] = {first_player}.play_card('Club',2)")
        print(f"{first_player} has played Club-2 to start the game")
        play_dict[first_player] = selected_card_dict['recent_card']
        #here we need a function that updates each players knowledge
        player_actions.update_player_knowledge(player1, player2, player3, player4, first_player, 'Club', 2, 'Club', True, False, game_data.score_dict)
        for i in range(len(play_list['play_order'])):
            if i == 0:
                pass
            else:
                exec(f"cur_player_dict['cur_player'] = play_list['play_order'][{i}]")
                print(cur_player_dict)
                valid_options = player_actions.identify_card_to_player(cur_player_dict['cur_player'], 'Club', first_turn, False)
                print(f"The valid options for {cur_player_dict['cur_player'].name} are:")
                for card in valid_options:
                    print(f"{card.suit}-{card.rank}")

                #NOW WE INSERT OUR RANDOM PLAY FUNCTION
                chosen_card = cur_player_dict['cur_player'].testing_randomchoice(valid_options)
                print(f"Player {cur_player_dict['cur_player'].name} has chosen to play {chosen_card.suit}, {chosen_card.rank}")
                #control to check if the game has been broken:

                selected_card_dict['recent_card'] = cur_player_dict['cur_player'].play_card(chosen_card.suit, chosen_card.rank)
                player_name_holder = cur_player_dict['cur_player'].name
                play_dict[player_name_holder] = selected_card_dict['recent_card']
                if chosen_card.suit == 'Club':
                    followed_suit = True
                else:
                    followed_suit = False
                if i == 3:
                    #FUNCTION NEEDS TO GO HERE TO UPDATE SCORE DICT
                    winner = game_data.calculate_score(play_dict, 'Club')
                    final_play = True
                else:
                    final_play = False
                player_actions.update_player_knowledge(player1, player2, player3, player4, cur_player_dict['cur_player'].name, chosen_card.suit,
                                                       chosen_card.rank, 'Club', followed_suit, final_play, game_data.score_dict)
        print(f"{winner} won the hand")
        #reset all players first to play to 0
        player1.first_to_play = 0
        player2.first_to_play = 0
        player3.first_to_play = 0
        player4.first_to_play = 0
        player1.reset_players_left_to_play()
        player2.reset_players_left_to_play()
        player3.reset_players_left_to_play()
        player4.reset_players_left_to_play()

        #since we're now returning a string of the name, switch back to exec
        exec(f"{winner}.first_to_play = 1")
        print(f" player 1 to play = {player1.first_to_play}")
        print(f" player 2 to play = {player2.first_to_play}")
        print(f" player 3 to play = {player3.first_to_play}")
        print(f" player 4 to play = {player4.first_to_play}")

        cards_remaining = len(player1.hand)
        first_turn = 0
        broken = False
        everbroken = False
        return cards_remaining, first_turn, broken, everbroken
    else:
        #play as normal
        for i in range(len(play_list['play_order'])):
            if i == 0:
                exec(f"cur_player_dict['cur_player'] = play_list['play_order'][{i}]")
                print(cur_player_dict)
                valid_options = player_actions.identify_card_to_player(cur_player_dict['cur_player'], False, first_turn, broken)
                print(f"The valid options for {cur_player_dict['cur_player'].name} are:")
                for card in valid_options:
                    print(f"{card.suit}-{card.rank}")

                # NOW WE INSERT OUR RANDOM PLAY FUNCTION
                chosen_card = cur_player_dict['cur_player'].testing_randomchoice(valid_options)
                print(
                    f"Player {cur_player_dict['cur_player'].name} has chosen to play {chosen_card.suit}, {chosen_card.rank}")

                #forces the first card into being the suit for the hand
                hand_suit = chosen_card.suit

                selected_card_dict['recent_card'] = cur_player_dict['cur_player'].play_card(chosen_card.suit,
                                                                                            chosen_card.rank)
                player_name_holder = cur_player_dict['cur_player'].name
                play_dict[player_name_holder] = selected_card_dict['recent_card']

                player_actions.update_player_knowledge(player1, player2, player3, player4,
                                                       cur_player_dict['cur_player'].name, chosen_card.suit,
                                                       chosen_card.rank, hand_suit, True, False,
                                                       game_data.score_dict)

            else:
                exec(f"cur_player_dict['cur_player'] = play_list['play_order'][{i}]")
                print(cur_player_dict)
                valid_options = player_actions.identify_card_to_player(cur_player_dict['cur_player'], hand_suit, first_turn, broken)
                print(f"The valid options for {cur_player_dict['cur_player'].name} are:")
                for card in valid_options:
                    print(f"{card.suit}-{card.rank}")

                #NOW WE INSERT OUR RANDOM PLAY FUNCTION
                chosen_card = cur_player_dict['cur_player'].testing_randomchoice(valid_options)
                print(f"Player {cur_player_dict['cur_player'].name} has chosen to play {chosen_card.suit}, {chosen_card.rank}")
                #if everbroken, pass, if not, if breaks, true
                if everbroken:
                    pass
                else:
                    if chosen_card.suit == 'Heart':
                        broken = True
                        everbroken = True
                selected_card_dict['recent_card'] = cur_player_dict['cur_player'].play_card(chosen_card.suit, chosen_card.rank)
                player_name_holder = cur_player_dict['cur_player'].name
                play_dict[player_name_holder] = selected_card_dict['recent_card']
                if chosen_card.suit == hand_suit:
                    followed_suit = True
                else:
                    followed_suit = False
                if i == 3:
                    #FUNCTION NEEDS TO GO HERE TO UPDATE SCORE DICT
                    winner = game_data.calculate_score(play_dict, hand_suit)
                    final_play = True
                else:
                    final_play = False
                player_actions.update_player_knowledge(player1, player2, player3, player4, cur_player_dict['cur_player'].name, chosen_card.suit,
                                                       chosen_card.rank, hand_suit, followed_suit, final_play, game_data.score_dict)
        print(f"{winner} won the hand")
        #reset all players first to play to 0
        player1.first_to_play = 0
        player2.first_to_play = 0
        player3.first_to_play = 0
        player4.first_to_play = 0
        player1.reset_players_left_to_play()
        player2.reset_players_left_to_play()
        player3.reset_players_left_to_play()
        player4.reset_players_left_to_play()
        #switching to exec as winner is now a name
        exec(f"{winner}.first_to_play = 1")
        print(f" player 1 to play = {player1.first_to_play}")
        print(f" player 2 to play = {player2.first_to_play}")
        print(f" player 3 to play = {player3.first_to_play}")
        print(f" player 4 to play = {player4.first_to_play}")

        cards_remaining = len(player1.hand)
        first_turn = 0
        return cards_remaining, first_turn, broken, everbroken





