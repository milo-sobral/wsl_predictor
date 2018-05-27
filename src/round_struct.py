# will hold a round's information
import collections

class Round :

    def __init__(self, round, heats) :
        self.round = round
        self.heats = heats


    def __repr__(self) :
        str = 'Round : {}\n'.format(self.round)
        for heat in self.heats :
            str += heat.__repr__()

        return str
