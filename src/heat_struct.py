# A class to hold information about a heat
import collections

Surfer = collections.namedtuple('Surfer', 'name, waves')

class Heat :
    round = str
    surfers = []
    heat_nb = int
