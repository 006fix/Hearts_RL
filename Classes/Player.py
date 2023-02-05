import pandas as pd

class Player():

    def __init__(self, name, score, hand):
        self.name = name
        self.score = score
        self.hand = hand

    #now we need a function to determine what cards the player holds, in a format a NN can read
    #we also need a function to determine knowledge about what cards remain
    #and a function to determine what is know about each players hand