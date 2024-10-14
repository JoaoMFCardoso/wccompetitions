from src.data import competition_points
import random
        
class Competition:
    def __init__(self,
                  name,
                  region,
                  division,
                  field_size,
                  points_per_position,
                  points_multiplier,
                  min_number_of_promotions,
                  number_of_promotions,
                  min_number_of_relegations,
                  number_of_relegations,
                  number_of_eligible):
        self.name = name
        self.region = region
        self.division = division
        self.field_size = field_size
        self.points_per_position = competition_points
        self.points_multiplier = points_multiplier
        self.final_rankings = []
        self.min_number_of_promotions = min_number_of_promotions
        self.number_of_promotions = number_of_promotions
        self.promoted_countries = []
        self.min_number_of_relegations = min_number_of_relegations
        self.number_of_relegations = number_of_relegations
        self.relegated_countries = []
        self.number_of_eligible = number_of_eligible
        self.eligible_countries = []
        
    def runCompetition(self, countries, eligible_countries):
        
        # Establishing the criteria for A division competitions and all the others
        qualified_countries = []
        match(self.name):
            case "World Championships":
                for country in countries:
                    if country.division == 1:
                        qualified_countries.append(country)
                        continue

            case "Pan Continental Nations League A":
                for country in countries:
                    if country.division == 1 and (country.region == 2 or country.region == 3):
                        qualified_countries.append(country)
                        continue
            
                if len(qualified_countries) < 8:
                    for eligible_country in eligible_countries:
                        if eligible_country not in qualified_countries and len(qualified_countries) < 8:
                            qualified_countries.append(eligible_country)
                            continue

            case "European Nations League A":
                for country in countries:
                    if country.division == 1 and country.region == 1:
                        qualified_countries.append(country)
                        continue

                if len(qualified_countries) < 10:
                    for eligible_country in eligible_countries:
                        if eligible_country not in qualified_countries and len(qualified_countries) < 10:
                            qualified_countries.append(eligible_country)
                            continue
            case _:
                for country in countries:
                    if country.region == self.region and country.division == self.division:
                        qualified_countries.append(country)
                        continue
        
        # randomly rank countries
        random.shuffle(qualified_countries)
        self.final_rankings = {country: rank + 1 for rank, country in enumerate(qualified_countries)}
        self.promoted_countries = sorted(self.final_rankings, key=self.final_rankings.get)[:self.number_of_promotions]
        self.relegated_countries = sorted(self.final_rankings, key=self.final_rankings.get, reverse=True)[:self.number_of_relegations]
        self.eligible_countries = sorted(self.final_rankings, key=self.final_rankings.get)[:self.number_of_eligible]