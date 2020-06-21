import json


class Person:
    def __init__(self, name, species, type, rank, sabercolor=None):
        super().__init__()
        self.name = name
        self.species = species
        self.type = type
        self.rank = rank
        if sabercolor:
            self.sabercolor = sabercolor

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
