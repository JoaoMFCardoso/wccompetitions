from src.data.input_data import weight_for_points, weight_for_ranking


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

def getTotalCountryPoints(points_list):
    total_points = 0.0
    for points_year in points_list:
        total_points = total_points + points_year
    return total_points


def getIndexByCountryName(countries, country_name):
    for index, country in enumerate(countries):
        if country.name == country_name:
            return index
    return -1