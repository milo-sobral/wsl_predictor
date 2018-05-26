# scraping the worldsurfleague.com website to gather data
import requests
import bs4
import json
from heat_struct import Heat, Surfer

def data_from_page(url) :
    html = get_html_from_web(url)
    data = get_heat_info(html)
    # create heat object
    # store object into JSON file
    return data

# get html info from web
def get_html_from_web(url) :
    html = requests.get(url)
    # print(html.text)
    return html.text

def get_round_info(html) :
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup_heats = soup.find_all('div', {'class' : 'new-heat'})
    

#get info about one head
def get_heat_info(html) :

    round = soup.find(class_='is-selected').find('strong').get_text()
    heat = soup.find(class_ = 'new-heat-hd-name').get_text()

    soup_surfers = soup.find_all("div",{"class":"new-heat-athlete-content-wrap"})
    soup_waves = soup.find_all("div", {"class" : "all-waves"})

    surfers = []
    for soup_surfer, soup_wave in zip(soup_surfers, soup_waves) :
            surfer = get_surfer_info(soup_surfer, soup_wave)
            surfers.append(surfer)

    print('round : ' + round)
    print('heat : ' + heat)

    for s in surfers :
        print(s)

    return round

#get the info about one surfer
def get_surfer_info(soup_surfer, soup_wave) :

    name = soup_surfer.find(class_ = 'avatar-text-primary').get_text()
    waves = []

    waves_soup_temp = soup_wave.find_all('span', {'class' : 'wave'})
    for w in waves_soup_temp :
        try :
            score = float(w.find(class_ = 'score').get_text())
        except Exception :
            score = None
        waves.append(score)

    surfer = Surfer(name = name, waves = waves)
    return surfer


def main() :
    data = data_from_page('http://www.worldsurfleague.com/events/2008/mct/4/quiksilver-pro-gold-coast?roundId=71')


if __name__ == '__main__' :
    main()
