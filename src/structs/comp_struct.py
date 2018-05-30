# holds info about a competition
import datetime
import json

class Competition :

    # TODO : Add meteo conditions

    def __init__(self, name, date, location, rounds):
        self.name = name
        self.date = date
        self.location = location
        self.rounds = rounds


    def __repr__(self) :
        str = 'COMPETITION : {}\n'.format(self.name)
        str += 'DATE : {}\nLOCATION : {} '.format(
            self.date,
            self.location
        )
        return str


    def to_json(self) :
        jsonized_rounds = [
            round.to_json()
            for round in self.rounds
        ]

        dict_comp = {
            'name' : self.name,
            'date' : self.date,
            'location' : self.location,
            'rounds' : jsonized_rounds
        }

        return dict_comp

    @staticmethod
    def from_json(comp_dict) :
        comp_object = Competition(
            name = comp_dict['name'],
            date = comp_dict['date'],
            location = comp_dict['location'],
            rounds = [
                Round.from_json(round)
                for round in comp_dict['rounds']
            ]
        )
        return comp_object
