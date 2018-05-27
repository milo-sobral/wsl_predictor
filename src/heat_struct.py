# A class to hold information about a heat
import collections

Surfer = collections.namedtuple('Surfer', 'name, waves')

class Heat :

    def __init__(self, round, heat, surfers) :
        self.round = round
        self.heat = heat
        self.surfers = surfers


    def __repr__(self) :
        print('-------------')
        print('Heat {} of {} : '.format(self.heat, self.round))
        for s in self.surfers :
            print('Name : {}\nWaves : \n\t{}\t'.format(s.name, s.waves))
