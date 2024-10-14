import random

class Region:
    def __init__(self, name, identifier, number_of_divisions, promotion_spots):
        self.name = name
        self.identifier = identifier
        self.number_of_divisions = number_of_divisions
        self.promotion_spots = promotion_spots
    
    def __str__(self):
        return f"Region {self.identifier}, {self.name}, Number of Divisions {self.number_of_divisions}"

class Country:
    def __init__(self, name, region, division):
        self.name = name
        self.region = region
        self.division = division
        
        
    def __str__(self):
        return f"{self.name}, Region {self.region}, Division {self.division}"
        
class Competition:
    def __init__(self, name, region, division, number_of_promotions, number_of_relegations, number_of_eligible):
        self.name = name
        self.region = region
        self.division = division
        self.final_rankings = []
        self.number_of_promotions = number_of_promotions
        self.promoted_countries = []
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

# Prints the results of a competition
def printResults(competition):
    for obj in competition.final_rankings:
        print(f"{obj} is ranked {competition.final_rankings[obj]}")
        
# Adjusts the division of a given country by -1 (thus promoting it)
def promoteCountry(promoted_countries, countries):
    for country in countries:
        for promoted_country in promoted_countries:
            if promoted_country.name == country.name:
                country.division = country.division - 1

# Adjusts the division of a given country by +1 (thus relegating it)
def relegateCountry(relegated_countries, countries):
    for country in countries:
        for relegated_country in relegated_countries:
            if relegated_country.name == country.name:
                country.division = country.division + 1

# Counts the number of countries in a given division and region
def countCountriesInDivisionRegion(countries, division, region):
    counter = 0
    for country in countries:
        if country.division == division and country.region == region:
            counter = counter + 1
    return counter

# Creates a dictionary with the region as key and number of countries from that region in the provided list
def countriesPerRegion(countries):
    countries_per_region = {1: 0, 2: 0, 3: 0}
    for country in countries:
        match(country.region):
            case 1: # Europe
                countries_per_region[1] = countries_per_region[1] + 1
                continue
            case 2: # Americas
                countries_per_region[2] = countries_per_region[2] + 1
                continue
            case 3: # Asia Pacific
                countries_per_region[3] = countries_per_region[3] + 1
                continue
    return countries_per_region