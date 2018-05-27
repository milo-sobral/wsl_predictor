# holds info about a competition

class Competition :

    def __init__(self, name, number, date, location, meteo_conditions, rounds) :
        self.name = name
        self.date = date
        self.location = location
        self.meteo_conditions = meteo_conditions
        self.rounds = rounds


    def __repr__(self) :
        str = 'COMPETITION {} : {}\n'.format(self.number, self.name)
        str += '\nDATE : {}\nLOCATION : {}\nCONDITIONS : {}'.format(
            self.date,
            self.location,
            self.meteo_conditions)
        return str
