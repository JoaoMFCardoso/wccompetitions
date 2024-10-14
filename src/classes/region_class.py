
class Region:
    def __init__(self,
                 name,
                 identifier,
                 number_of_divisions,
                 promotion_spots):
        self.name = name
        self.identifier = identifier
        self.number_of_divisions = number_of_divisions
        self.promotion_spots = promotion_spots
    
    def __str__(self):
        return f"Region {self.identifier}, {self.name}, Number of Divisions {self.number_of_divisions}"