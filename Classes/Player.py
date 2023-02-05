import pandas as pd

class Player():

    def __init__(self, name, score, hand):
        self.name = name
        self.score = score
        self.hand = hand

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
            'hands_played',
            'score_altplayer1',
            'score_altplayer2',
            'score_altplayer3',
            'left_to_play_altplayer1',
            'left_to_play_altplayer2',
            'left_to_play_altplayer3',
            'total_players_left_toplay',
            'alt_player1_clubs',
            'alt_player1_hearts',
            'alt_player1_spades',
            'alt_player1_diamonds',
            'alt_player2_clubs',
            'alt_player2_hearts',
            'alt_player2_spades',
            'alt_player2_diamonds',
            'alt_player3_clubs',
            'alt_player3_hearts',
            'alt_player3_spades',
            'alt_player3_diamonds']

        self.tertiary_values = {}

        for i in list_of_values:
            self.tertiary_values[i] = 0


