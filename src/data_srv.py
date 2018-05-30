# Provides methods to gather useful info about the database
import collections
import sys
import os
path_to_structs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'structs')
sys.path.insert(0, path_to_structs)
from heat_struct import Heat, Surfer
from round_struct import Round
from comp_struct import Competition

History = collections.namedtuple('History', 'comp, nb_years, standings, lost_against')


def get_surfers_list(year) :
    surfer_list = set()
    for comp in year :
        surfers = comp.get_surfers()
        surfer_list.add(surfer for surfer in comp.get_surfers())

    return surfers


def get_surfer_results(year, year_end = 0) :
    return results


def get_surfer_best_score(year, year_end = 0) :
    return results


def get_comp_meteo(comp) :
    return meteo


def get_comp_standing(comp) :
    return standing


def get_year_best_heats(year, year_end = 0) :
    return best_heats


def get_surfer_best_heats(year, year_end = 0) :
    return best_heats


def get_all_matchups(surfer_name1, surfer_name2) :
    return matchup_heats


def get_surfer_number_waves(surfer) :
    return wave_number


def get_surfer_history(comp) :
    return surfer_history
