# scraping the worldsurfleague.com website to gather data
import requests
import bs4
import sys
import os
import time
import json

path_to_structs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'structs')
sys.path.insert(0, path_to_structs)

from heat_struct import Heat, Surfer
from round_struct import Round
from comp_struct import Competition

#global variables
TIME_DELTA = 5

# given a base url for a competition, returns a competition object
def get_competition_info(base_url) :

    print('\nquerying {}  ...'.format(base_url))
    html = get_html_from_web(base_url)
    print('DONE\nRetrieving round urls...')
    urls = get_url_list(html)
    print('DONE\n')
    rounds = []
    for url in urls :
        html = get_html_from_web(url)
        print('querying {}  ...'.format(url))
        round_temp = get_round_info(html)
        print('parsing...')
        rounds.append(round_temp)
        print('{} DONE'.format(round_temp.round))
        time.sleep(TIME_DELTA)

    name, date, location = get_comp_basic_info(html)
    comp = Competition(name = name, date = date, location = location, rounds = rounds)

    return comp


# Get basic info about a competition
def get_comp_basic_info(html) :
    soup = bs4.BeautifulSoup(html, 'lxml')
    name = soup.find(class_ = 'event-title').h1.get_text()
    date = soup.find(class_ = 'event-schedule-primary').get_text()
    location = soup.find(class_ = 'event-meta').get_text()
    return name, date, parse_location(location)


# parsing useful info out of the raw location division
def parse_location(raw) :
    words = raw.split(' ')
    words = words[4:]
    str = ''
    for word in words :
        str += word + ' '
    return str


# takes an html pages, parses the info about the round, gives back a Round object
def get_round_info(html) :
    soup = bs4.BeautifulSoup(html, 'lxml')
    soup_heats = soup.find_all('div', class_ = 'new-heat')

    round = soup.find(class_='carousel').find(match_class(['carousel-item', 'is-selected'])).find('strong').get_text()

    list_heats = []
    heat_nb = 1
    for soup_heat in soup_heats :
        list_heats.append(get_heat_info(soup_heat, heat_nb, round))
        heat_nb += 1

    current_round = Round(round, list_heats)

    return current_round


# takes an html div soup, parses info about a Heat, gives back a filled Heat object
def get_heat_info(soup, heat_nb, round) :

    temp = soup.find(class_ = 'content').find(class_ = 'bd').find_all('div', recursive = False)
    soup_athletes = soup.find_all("div",{"class":"new-heat-athlete"})

    list_surfers = []
    for soup_athlete in soup_athletes :
        surfer = get_surfer_info(soup_athlete)
        list_surfers.append(surfer)

    current_heat = Heat(round, heat_nb, list_surfers)
    return current_heat


# takes an html div soup, parses info about a surfer's performance, gives back a filled Surfer namedtuple
def get_surfer_info(soup) :

    soup_surfer = soup.find("div",{"class":"new-heat-athlete-content-wrap"})
    soup_wave = soup.find('div', {'class' : 'all-waves'})

    name = soup_surfer.find(class_ = 'avatar-text-primary').get_text()
    list_waves = []
    waves_soup_temp = soup_wave.find_all('span', {'class' : 'wave'})

    for w in waves_soup_temp :
        try :
            score = float(w.find(class_ = 'score').get_text())
        except AttributeError :
            continue
        list_waves.append(score)

    wave1, wave2 = two_largest(list_waves)
    total = wave1 + wave2

    surfer = Surfer(name = name, waves = list_waves, total = total)

    return surfer


# get html info from web
def get_html_from_web(url) :
    try :
        html = requests.get(url)
    except requests.exceptions.ConnectionError :
        print('Network is down. Cannot connect to host.\n')
        exit(1)
    return html.text


#  Helper method to parse soup objects
def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


def two_largest(inlist):
    """Return the two largest items in the sequence. The sequence must
    contain at least two items."""
    largest = 0
    second_largest = 0

    if len(inlist) < 2 :
        return 0, 0

    for item in inlist:
        if item > largest:
            largest = item
        elif largest > item > second_largest:
            second_largest = item
    # Return the results as a tuple
    return largest, second_largest


#  Returns a list of all urls nedded to visit one competition
def get_url_list(html) :
    soup = bs4.BeautifulSoup(html, 'lxml')

    url_base = 'http://www.worldsurfleague.com'
    list_url = soup.find('div', {'class' : 'carousel'}).find_all('li')

    final_list = []
    for l in list_url :
        final_list.append(url_base + l['data-item-href'])

    return final_list


#  Get the path where a json file for one competition will be saved
def get_json_path(comp, path) :
    current_path = os.path.dirname(os.path.abspath(__file__))

    if not path :
        temp = os.path.join(os.path.split(os.path.split(current_path)[0])[0],'wsl_predictor_bin')
        if not os.path.isdir(temp) :
            os.mkdir(temp)
        json_files = os.path.join(os.path.split(os.path.split(current_path)[0])[0],'wsl_predictor_bin', 'json_data')
    else :
        path = os.path.abspath(path)
        json_files = os.path.join(path, 'json_data')

    if not os.path.isdir(json_files) :
        os.mkdir(json_files)

    comp_year = comp.date.split()[-1]
    comp_name = comp.name.replace(' ', '_')

    sub_year = os.path.join(json_files, comp_year)
    if not os.path.isdir(sub_year) :
        os.mkdir(sub_year)
    final_sub_path = os.path.join(sub_year, comp_name + '.json')
    return final_sub_path


#  Write a comp object to a json file
def write_to_json(comp, path) :
    json_path = get_json_path(comp, path)
    with open(json_path, 'w') as fout :
        print('\ndumping to JSON file at {}'.format(json_path))
        json.dump(comp.to_json(), fout, indent = 2)
        print('DONE')


def main(base_url) :
    comp = get_competition_info(base_url)
    write_to_json(comp)


if __name__ == '__main__' :
    url = input('url : ')
    main(url)
