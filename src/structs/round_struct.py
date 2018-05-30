# will hold a round's information
import collections
import sys
import os
path_to_program = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path_to_program)
from heat_struct import Heat, Surfer

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


    # transforms into dictionaries
    def to_json(self) :

        jsonized_heats = [
            heat.to_json()
            for heat in self.heats
        ]

        dict_round = {
            'round' : self.round,
            'heats' : jsonized_heats
        }

        return dict_round

    @staticmethod
    def from_json(round_dict) :
        round_object = Round(
            round = round_dict['round'],
            heats = [
                Heat.from_json(heat)
                for heat in round_dict['heats']
            ]
        )
        return round_object
