# scraping the worldsurfleague.com website to gather data
import requests
import bs4
import json
from heat_struct import Heat, Surfer

def data_from_page(url) :
    html = get_html_from_web(url)
    data = gather_page_info(html)
    # create heat object
    # store object into JSON file
    return data

def get_html_from_web(url) :
    html = requests.get(url)
    # print(html.text)
    return html.text


def gather_page_info(html) :
    soup = bs4.BeautifulSoup(html, 'html.parser')
    Round = soup.find(class_='is-selected').find('strong').get_text()
    Surfer1 = Surfer(name = soup.find(class_ = 'avatar-text-primary').get_text())
    print(Surfer1)

    return Round


def main() :
    print(data_from_page('http://www.worldsurfleague.com/events/2008/mct/4/quiksilver-pro-gold-coast?roundId=71'))


if __name__ == '__main__' :
    main()
