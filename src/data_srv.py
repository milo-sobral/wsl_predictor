# Provides methods to gather useful info about the database
import collections

History = collections.namedtuple('History', 'comp, nb_years, standings, lost_against')


def get_surfers_list(year, year_end = 0) :
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
