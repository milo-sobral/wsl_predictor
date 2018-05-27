# will hold a round's information
import collections

class Round :
    def __init__(self, round, heats) :
        self.round = round
        self.heats = heats


    def __repr__(self) :
        print('Round : {}\n')
        for heat in heats : 
            print(heat)
