from src.data.input_data import weight_for_ranking, weight_for_points


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
        total_points = 0.0
        for points_year in self.points:
            total_points = total_points + points_year
        self.strength = weight_for_ranking * (1 / self.rank) + weight_for_points * total_points
        
        
    def __str__(self):
        return f"{self.name}, Region {self.region}, Division {self.division}"

    def updateRank(self, new_rank):
        self.rank = new_rank
        self.calculateStrength()

    def updatePoints(self, new_points):
        self.points = new_points
        self.calculateStrength()
    
    def calculateStrength(self):
        # Calculate total points
        total_points = 0.0
        for points_year in self.points:
            total_points = total_points + points_year

        self.strength = weight_for_ranking * (1 / self.rank) + weight_for_points * total_points
        