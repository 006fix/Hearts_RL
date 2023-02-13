

import Functions.Populate_Players as pop_players
import Game_Space.Playing_Table as game_data
import Functions.Playing_Hands as play_hand
import Functions.Game_Start_Function_Sequence as game_start
import copy
import Functions.testing_alt_player_naming as test_names

#THIS CAN NOW PLAY 5 GAMES AT ONCE, BUT DO I WANT IT TO?
#ALLOWS FOR BETTER CONTROL OF RANDOMNESS, BUT MEANS THE INDIVIDUAL PLAY OF AN INDIVIDUAL HAND NOW HAS EVEN LESS WEIGHTING ON THE FINAL SCORE
#probably remove later.

game_data.score_dict = {'player1': 0, 'player2': 0, 'player3': 0, 'player4': 0}
game_data.played_cards = []
player1, player2, player3, player4 = pop_players.create_players()
game_start.game_start_func_sequence(player1, player2, player3, player4)

#testing sequence for alt player names
test_names.test_alt_players(player1, player2, player3, player4)

#with all players updated, we now need a function to run hands of the game
turn_counter = 0
everbroken = False
broken = False
first_turn = 1
cards_remaining = 13
while cards_remaining >0:
    turn_counter += 1
    print(f"Now commencing turn {turn_counter}")
    cards_remaining, first_turn, broken, everbroken = play_hand.play_hand(player1, player2, player3, player4, first_turn, broken, everbroken)
    print(cards_remaining)
    #CONTROL CHECK TO MAKE SURE THAT CARDS ARE BEING PLAYED PROPERLY
    print(f"At the end of turn {turn_counter}, hand sizes are as follows:")
    print(f"Player 1 has {len(player1.hand)} cards remaining")
    print(f"Player 2 has {len(player2.hand)} cards remaining")
    print(f"Player 3 has {len(player3.hand)} cards remaining")
    print(f"Player 4 has {len(player4.hand)} cards remaining")
    print(f"At the end of this turn, the everbroken status is {everbroken} and the broken status is {broken}")
    print(f"At the end of this turn, the scores are {game_data.score_dict}")


print(f"At the end of the game, the scores are {game_data.score_dict}")
