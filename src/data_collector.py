# scraping the worldsurfleague.com website to gather data
import requests
import bs4
from heat_struct import Heat, Surfer
from round_struct import Round

# takes an html pages, parses the info about the round, gives back a Round object
def get_round_info(html) :
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup_heats = soup.find_all('div', {'class' : 'new-heat'})

    list_heats = []
    for soup_heat in soup_heats :
        list_heats.append(get_heat_info(soup_heat))

    round = list_heats[0].round

    current_round = Round(round, list_heats)

    return current_round


# takes an html div soup, parses info about a Heat, gives back a filled Heat object
def get_heat_info(html) :

    round = soup.find(class_='is-selected').find('strong').get_text()
    heat = soup.find(class_ = 'new-heat-hd-name').get_text()

    soup_surfers = soup.find_all("div",{"class":"new-heat-athlete-content-wrap"})
    soup_waves = soup.find_all("div", {"class" : "all-waves"})

    list_surfers = []
    for soup_surfer, soup_wave in zip(soup_surfers, soup_waves) :
            surfer = get_surfer_info(soup_surfer, soup_wave)
            list_surfers.append(surfer)

    current_heat = Heat(round, heat, list_surfers)

    return current_heat


# takes an html div soup, parses info about a surfer's performance, gives back a filled Surfer namedtuple
def get_surfer_info(soup_surfer, soup_wave) :

    name = soup_surfer.find(class_ = 'avatar-text-primary').get_text()
    list_waves = []

    waves_soup_temp = soup_wave.find_all('span', {'class' : 'wave'})
    for w in waves_soup_temp :
        try :
            score = float(w.find(class_ = 'score').get_text())
        except Exception :
            score = None
        list_waves.append(score)

    surfer = Surfer(name = name, waves = waves)

    return surfer


# get html info from web
def get_html_from_web(url) :
    html = requests.get(url)
    return html.text


def main(url) :
    html = get_html_from_web(url)
    data = data_from_page(html)

    return data


if __name__ == '__main__' :
    main('http://www.worldsurfleague.com/events/2008/mct/4/quiksilver-pro-gold-coast?roundId=71')
