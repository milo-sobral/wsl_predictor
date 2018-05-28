import round_data_colletor
path_to_structs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'structs')
sys.path.insert(0, path_to_structs)

from heat_struct import Heat, Surfer
from round_struct import Round
from comp_struct import Competition


def main(base_url) :
    list_year_urls = get_urls_years(base_url)
    for year_url in list_year_urls :
        list_comp_urls = get_urls_comp(url)
        for comp_url in list_comp_urls :
            comp = round_data_colletor.get_competition_info(comp_url)
            round_data_colletor.write_to_json(comp)


def get_urls_years(url) :
    pass


def get_urls_comp(url) :
    pass


if __name__ == '__main__' :
    main()
