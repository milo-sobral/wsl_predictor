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
    dataset_path = input('Where do you want to save your files?\n')
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
    start_year = input('What year do you want your dataset to begin with ? [2008-2017]  ')
    end_year = input('What year do you want your dataset to end with ? [2008-2017]  ')
    for i in range(int(start_year), int(end_year)+1) :
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
