
class Country:
    def __init__(self,
                 name,
                 region,
                 division,
                 rank,
                 points):
        self.name = name
        self.region = region
        self.division = division
        self.rank = rank
        self.points = points
        
        
    def __str__(self):
        return f"{self.name}, Region {self.region}, Division {self.division}"