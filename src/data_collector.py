import round_data_collector as rdc
import bs4 as bs
import os
import sys
path_to_structs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'structs')
sys.path.insert(0, path_to_structs)

from heat_struct import Heat, Surfer
from round_struct import Round
from comp_struct import Competition


def main() :
    bad_answer = True
    while bad_answer :
        dataset_path = input('Where do you want to save your files? ([enter] for default location)\n')
        if not os.path.isdir(dataset_path) and dataset_path:
            print('Folder {} not found'.format(dataset_path))
        else :
            bad_answer = False

    list_year_urls = get_urls_years()
    for year_url in list_year_urls :
        print('\nyear : ' + year_url + '\n')
        list_comp_urls = get_urls_comp(parse_from_url(year_url))
        for comp_url in list_comp_urls :
            print('comp : ' + comp_url)
            comp = rdc.get_competition_info(comp_url)
            rdc.write_to_json(comp, dataset_path)


def get_urls_years() :
    url_list = []
    start_year = ''
    end_year = ''
    bad_answer = True
    while bad_answer :
        try :
            start_year = int(input('What year do you want your dataset to begin with ? [2008-2017]  ').strip())
            end_year = int(input('What year do you want your dataset to end with ? [2008-2017]  ').strip())
        except ValueError :
            print('Enter years as valid integers')

        if not 2008 <= start_year <= 2017 or not 2008 <= end_year <= 2017:
            print('No info for provided years')
        elif start_year > end_year or not start_year or not end_year:
            print('please enter a working range and both limits')
        else :
            bad_answer = False

    for i in range(start_year, end_year+1) :
        url_list.append('http://www.worldsurfleague.com/events/{}/mct'.format(i))
    return url_list


def get_urls_comp(soup) :
    url_list = []
    soup_events = soup.find_all(class_ = 'tour-event')
    for soup_event in soup_events :
        url = soup_event.a['href']
        url_list.append(url)
    return url_list


def parse_from_url(url) :
    html = rdc.get_html_from_web(url)
    soup = bs.BeautifulSoup(html, 'lxml')
    return soup


if __name__ == '__main__' :
    main()
