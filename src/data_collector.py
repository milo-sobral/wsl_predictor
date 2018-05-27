# scraping the worldsurfleague.com website to gather data
import requests
import bs4
from heat_struct import Heat, Surfer
from round_struct import Round

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
    # print(soup_surfer)
    waves_soup_temp = soup_wave.find_all('span', {'class' : 'wave'})
    
    for w in waves_soup_temp :
        try :
            score = float(w.find(class_ = 'score').get_text())
        except Exception :
            score = None
        list_waves.append(score)

    wave1 = max(list_waves)
    list_copy = list_waves.remove(wave1)
    wave2 = max(list_copy)
    total = wave1 + wave2

    surfer = Surfer(name = name, waves = list_waves, total=total)

    return surfer


# get html info from web
def get_html_from_web(url) :
    html = requests.get(url)
    return html.text


def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


def main(url) :
    html = get_html_from_web(url)
    data = get_round_info(html)
    print(data)

    return data


if __name__ == '__main__' :
    main('http://www.worldsurfleague.com/events/2008/mct/4/quiksilver-pro-gold-coast?roundId=42')
