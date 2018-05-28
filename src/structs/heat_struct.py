# A class to hold information about a heat
import collections

Surfer = collections.namedtuple('Surfer', 'name, waves, total')

class Heat :

    def __init__(self, round, heat, surfers) :
        self.round = round
        self.heat = heat
        self.surfers = surfers


    def __repr__(self) :
        str = '\n-------------\n'
        str += 'Heat {} of {} : \n'.format(self.heat, self.round)
        for s in self.surfers :
            str += '\nName : {}\nWaves : \n\t{}\t\t'.format(s.name, s.waves)

        return str


    def get_heat_winner(self) :
        max = self.surfers[0]
        for surfer in self.surfers :
            if surfer.total > max.total :
                max = surfer
        return max


    def get_heat_best_wave(self) :
        max = self.surfers[0][0]
        for s in surfers :
            for w in s.waves :
                if w > max :
                    max = w
        return max


    # transform a heat object into a dictionary
    def to_json(self) :
        temp_surfers = []
        for surfer in self.surfers :
            dict_surfer = {
                'name' : surfer.name,
                'waves' : surfer.waves,
                'total' : surfer.total
            }
            temp_surfers.append(dict_surfer)

        dict_heat = {
            'round' : self.round,
            'heat' : self.round,
            'surfers' : temp_surfers
        }

        return dict_heat
