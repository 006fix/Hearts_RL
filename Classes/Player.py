import pandas as pd
import Game_Space.Playing_Table as game_data
import random

class Player():

    def __init__(self, name, score, hand):
        self.name = name
        self.score = score
        self.hand = hand

        if self.name == 'player1':
            self.alt_player1 = 'player2'
            self.alt_player2 = 'player3'
            self.alt_player3 = 'player4'
        elif self.name == 'player2':
            self.alt_player1 = 'player3'
            self.alt_player2 = 'player4'
            self.alt_player3 = 'player1'
        elif self.name == 'player3':
            self.alt_player1 = 'player4'
            self.alt_player2 = 'player1'
            self.alt_player3 = 'player2'
        elif self.name == 'player4':
            self.alt_player1 = 'player1'
            self.alt_player2 = 'player2'
            self.alt_player3 = 'player3'
        else:
            raise ValueError("I believe player names have been provided incorrectly, please review")

        self.alt_player_dict = {'alt_player1': self.alt_player1, 'alt_player2': self.alt_player2, 'alt_player3': self.alt_player3}


    #now we need a function to determine what cards the player holds, in a format a NN can read
        #PARTIALLY COMPLETE, JUST NEEDS TO BE TRANSALTED FROM A DICT INTO A DATAFRAME
    #we also need a function to determine knowledge about what cards remain
        #PARTIALLY COMPLETE, JUST NEEDS TO BE TRANSALTED FROM A DICT INTO A DATAFRAME
    #and a function to determine what is know about each players hand
        #TBC

    #beyond this, we also need information on generic traits relating to each player
    #score - stores current store of each player
    #left to play? stores values for each of the players, showing if they still have yet to play this hand
        #beyond this, generic value for how many total players are left to play
    #finally, for each player, for each suit, a record of if they still have that suit left

    def initial_generate_data(self):
        self.firt_to_play = 0
        self.self_cards = {}
        self.other_cards = {}

        suits = ['Heart', 'Club', 'Spade', 'Diamond']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for i in suits:
            for j in ranks:
                holdstr = i + "-" + str(j)
                self.self_cards[holdstr] = 0
                #initially, set all other cards to 1, switch to zero later
                self.other_cards[holdstr] = 1

    def first_populate_data(self):

        for card in self.hand:
            holdstr = card.suit + "-" + str(card.rank)
            self.self_cards[holdstr] = 1
            self.other_cards[holdstr] = 0

    def initial_other_knowledge(self):

        list_of_values = [
            #vars below update at end of each hand
            'hands_played',
            'score_alt_player1',
            'score_alt_player2',
            'score_alt_player3',
            'score_self',
            #vars below update every time someone plays a card
            'left_to_play_alt_player1',
            'left_to_play_alt_player2',
            'left_to_play_alt_player3',
            'total_players_left_to_play',
            'alt_player1_Club',
            'alt_player1_Heart',
            'alt_player1_Spade',
            'alt_player1_Diamond',
            'alt_player2_Club',
            'alt_player2_Heart',
            'alt_player2_Spade',
            'alt_player2_Diamond',
            'alt_player3_Club',
            'alt_player3_Heart',
            'alt_player3_Spade',
            'alt_player3_Diamond']

        self.tertiary_values = {}

        for i in list_of_values:
            self.tertiary_values[i] = 0

    def first_to_play(self):

        for card in self.hand:
            if card.suit == 'Club':
                if card.rank == 2:
                    self.first_to_play = 1


    def play_card(self, card_suit, card_rank):

        selected_index = 0

        #using this method to get an index value, to later remove
        for i in range(len(self.hand)):
            hold_card = self.hand[i]
            if hold_card.rank == card_rank:
                if hold_card.suit == card_suit:
                    selected_index = i


        selected_card = self.hand[selected_index]
        game_data.played_cards.append(selected_card)
        del self.hand[selected_index]

        return selected_card

        ##NOTE - AT THIS POINT WE NOW NEED TO IMPLEMENT A FUNCTION TO UPDATE ALL KNOWN VALUES
        #once this is done, the move should be appended to the list of moves.

    #this function runs at the end of every hand, and updates hand level scores
    def update_end_of_hand_scores(self, score_dict):

        holdval = 0

        for key in score_dict:
            if key == self.name:
                holdval = self.tertiary_values['score_self']
                holdval += score_dict[key]
                self.tertiary_values['score_self'] = holdval
            else:
                for item in self.alt_player_dict:
                    if key == self.alt_player_dict[item]:
                        exec(f"holdval = self.tertiary_values['score_{item}']")
                        holdval += score_dict[key]
                        exec(f"self.tertiary_values['score_{item}'] = holdval")


    def reset_players_left_to_play(self):
        #NB - THIS FUNCTION MUST BE CALLED AT THE END OF EACH HAND
        self.tertiary_values['left_to_play_alt_player1'] = 1
        self.tertiary_values['left_to_play_alt_player2'] = 1
        self.tertiary_values['left_to_play_alt_player3'] = 1
        self.tertiary_values['total_players_left_to_play'] = 3

    #call this at start of each game
    def update_alt_player_card_suits(self):
        val_list = ['alt_player1_Club',
            'alt_player1_Heart',
            'alt_player1_Spade',
            'alt_player1_Diamond',
            'alt_player2_Club',
            'alt_player2_Heart',
            'alt_player2_Spade',
            'alt_player2_Diamond',
            'alt_player3_Club',
            'alt_player3_Heart',
            'alt_player3_Spade',
            'alt_player3_Diamond']
        for val in val_list:
            self.tertiary_values[val] = 1

    #this function runs after every player plays, and updates intra-hand level scores
    def update_intra_hand_scores(self, player_played, card_suit, card_rank, start_suit, followed_suit):

        #WE NEED TO REMOVE FROM SELF.OTHER_CARDS, OR SELF.OWN_CARDS AS NEEDED
        holdval = f"{card_suit}-{card_rank}"
        if player_played == self.name:
            self.self_cards[holdval] = 0
        else:
            self.other_cards[holdval] = 0

        #now we need to update players_played appropriately
        if player_played == self.name:
            #if we played, no need to touch any of these variables
            pass
        else:
            #if others played, we need to update
            for item in self.alt_player_dict:
                if player_played == self.alt_player_dict[item]:
                    #easier than just referencing item
                    active_player = item
                    #set that player left_to_play = 0
                    exec(f"self.tertiary_values['left_to_play_{active_player}'] = 0")
                    #we also need to update suit held values if the player didn't follow suit
                    if followed_suit == False:
                        exec(f"self.tertiary_values['{active_player}_{start_suit}'] = 0")

    def update_knowledge(self, player_played, card_suit, card_rank, start_suit, followed_suit, hand_finished, score_dict):
        #to update hands played if required
        if hand_finished == True:
            holdval = self.tertiary_values['hands_played']
            holdval += 1
            self.tertiary_values['hands_played'] = holdval
            #WE NEED A FUNCTION ON SCORE DICT HERE TO UPDATE SCORES
            self.update_end_of_hand_scores(score_dict)
        else:
            self.update_intra_hand_scores(player_played, card_suit, card_rank, start_suit, followed_suit)

    #function to identify what cards could be played
    def identify_valid_cards(self, start_suit, first_turn, broken):

        valid_options = []

        for card in self.hand:
            if start_suit == False:
                if broken:
                    valid_options.append(card)
                else:
                    if card.suit == 'Heart':
                        pass
                    elif card.suit == 'Spade' and card.rank == 12:
                        pass
                    else:
                        valid_options.append(card)
            else:
                if card.suit == start_suit:
                    valid_options.append(card)

        #if we have no cards in the same suit
        if len(valid_options) == 0:
            for card in self.hand:
                if first_turn == 0:
                    valid_options.append(card)
                else:
                    #top 2 here exist for first turn no dump mechanics
                    if card.suit == 'Heart':
                        pass
                    elif card.suit == 'Spade' and card.rank == 12:
                        pass
                    else:
                        valid_options.append(card)

        return valid_options

    def testing_noclubs(self):
        #This function just exists to validate first turn drop mechanics
        #If the 2 of clubs is held, it will not run
        #Otherwise, the suit of all clubs is turned into diamonds.
        canrun = True

        for card in self.hand:
            if card.suit == 'Club':
                if card.rank == 2:
                    print("I'm afraid I'm unable to run as I hold the 2 of Clubs")
                    canrun = False

        if canrun:
            for i in range(len(self.hand)):
                if self.hand[i].suit == 'Club':
                    self.hand[i].suit = 'Diamond'

    #NEED A FUNCTION FOR WHAT TO PLAY IF PLAYING FIRST


    def testing_randomchoice(self, valid_options):

        random.shuffle(valid_options)
        chosen_card = valid_options[0]

        return chosen_card
