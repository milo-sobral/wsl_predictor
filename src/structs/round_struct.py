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


    def get_best_heat_total() :
        max = self.heats[0]
        for h in self.heats :
            if h.get_heat_winner().total > max.get_heat_winner().total :
                max = h
        return max
