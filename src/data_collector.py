# scraping the worldsurfleague.com website to gather data
import requests
import bs4
from heat_struct import Heat, Surfer
from round_struct import Round

# takes an html pages, parses the info about the round, gives back a Round object
def get_round_info(html) :
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup_heats = soup.find_all('div', class_ = 'new-heat')

    round = soup.find(class_='carousel').find(match_class(['carousel-item', 'is-selected'])).find('strong').get_text()

    # soup_waves = soup.find_all(class_='all-waves')
    # print(soup_waves)
    # soup_surfers = soup.find_all(class_ = "new-heat-athlete-content-wrap
    # print(round)

    # list_heats = []
    # for soup_heat in soup_heats :
    #     list_heats.append(get_heat_info(soup_heat, round))
    #     # print(soup_heat.find(class_='new-heat-hd-name').get_text())

    # for s in soup_heats :
    #     print(s.find(class_ = 'all-waves'))

    list_heats = []
    heat_nb = 1
    for soup_heat in soup_heats :
        # print(soup_heat)
        list_heats.append(get_heat_info(soup_heat, heat_nb, round))
        heat_nb += 1

    current_round = Round(round, list_heats)

    return current_round


# takes an html div soup, parses info about a Heat, gives back a filled Heat object
def get_heat_info(soup, heat_nb, round) :

    # round = soup.find(class_='is-selected').find('strong').get_text()
    # heat = soup.find(class_ = 'new-heat-hd-name').get_text()

    # soup_surfers = soup.find_all("div", {"class":"new-heat-athlete-content-wrap"})
    # # soup_waves = soup.find_all("div", {"class" : "all-waves"})
    # soup_waves = soup.find_all(match_class(['all-waves', 'all-waves-grid']))

    # print(soup_waves)
    #
    # list_surfers = []
    # for soup_surfer, soup_wave in zip(soup_surfers, soup_waves) :
    #         surfer = get_surfer_info(soup_surfer, soup_wave)
    #         list_surfers.append(surfer)

    temp = soup.find(class_ = 'content').find(class_ = 'bd').find_all('div', recursive = False)
    # print(len(temp))
    soup_athletes = soup.find_all("div",{"class":"new-heat-athlete"})
    #
    list_surfers = []
    for soup_athlete in soup_athletes :
        # print(soup_athlete.find(class_='new-heat-athlete-content-wrap').find(class_ = 'avatar-text-primary').get_text())
        surfer = get_surfer_info(soup_athlete)
        list_surfers.append(surfer)

    current_heat = Heat(round, heat_nb, list_surfers)
    # print(current_heat.surfers)
    return current_heat


# takes an html div soup, parses info about a surfer's performance, gives back a filled Surfer namedtuple
def get_surfer_info(soup) :

    # print(soup)

    soup_surfer = soup.find("div",{"class":"new-heat-athlete-content-wrap"})
    # soup_wave = soup.find(class_ = ''))

    name = soup_surfer.find(class_ = 'avatar-text-primary').get_text()
    list_waves = []
    # print(soup_surfer)
    waves_soup_temp = soup_surfer.find_all('span', {'class' : 'wave'})
    for w in waves_soup_temp :
        try :
            score = float(w.find(class_ = 'score').get_text())
        except Exception :
            score = None
        list_waves.append(score)

    surfer = Surfer(name = name, waves = list_waves)

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
    main('http://www.worldsurfleague.com/events/2008/mct/4/quiksilver-pro-gold-coast?roundId=48')
