import random
from src.utilities import getIndexByCountryName, getTotalCountryPoints
from src.data.input_data import weight_for_season_points, competition_points_multiplier, competition_points

# This function calculates the final standings of a competition randomly
# Input:
# participant_countries: A list of Country objects that are participating in this competition
# Output:
# final_rankings: A dictionary with rank as key and the Country object as value
def randomRankingCalculator(participant_countries):
    final_rankings = {}
    random.shuffle(participant_countries)
    final_rankings = {country: rank + 1 for rank, country in enumerate(participant_countries)}
    return final_rankings

# This function calculates the final standings of a competition based on each country's rank and points
# Input:
# participant_countries: A list of Country objects that are participating in this competition
# Output:
# final_rankings: A dictionary with rank as key and the Country object as value
def weightedRankingCalculator(participant_countries):
    final_rankings = {}
    
    #Calculate the strenght of each participant country
    strength_list = []
    total_strength = 0
    for country in participant_countries:
        country.calculateStrength()
        strength_list.append(country.strength)
        total_strength = total_strength + country.strength

    #Calculate probabilities by normalising the strenghts
    probabilities = []
    for strength in strength_list:
        probability = strength/total_strength
        probabilities.append(probability)

    #calculate the final standings based on each country's probabilities
    field = participant_countries
    field_size = len(participant_countries)
    final_rankings = {}
    rank = 1
    while len(final_rankings) < field_size:
        # select one country based on the pre-calculated probabilities
        selected_country = random.choices(field, probabilities) 

        # add selected country to final rankings
        final_rankings[selected_country[0]] = rank
        rank = rank + 1

        # Remove selected country from field and remove respective probability
        selected_country_index = field.index(selected_country[0])
        field.pop(selected_country_index)
        probabilities.pop(selected_country_index)

    return final_rankings

def preparePointsForCalculation(countries):
    for country in countries:
        quadrineal_points = country.points

        # The 4th year is eliminated, as points for that year are no longer counted
        quadrineal_points.pop(0)
        # Add the current year as 0.0
        quadrineal_points.append(0.0)
        # Recalculate the points for all years based on the weight_for_season_points
        new_quadrineal_points = [0.0, 0.0, 0.0, 0.0]
        for i in range(len(quadrineal_points)):
            new_quadrineal_points[i] = round(quadrineal_points[i] * weight_for_season_points[i], 3)
        country.points = new_quadrineal_points

def calculatePointsForCompetition(countries, competition_name, final_standings):
    
    # Calculate the points for this competition based on the multiplier
    points_for_competition = []
    for i in range(len(final_standings)):
        points_for_competition.append(competition_points[i + 1] * competition_points_multiplier[competition_name])
    
    # Calculate the points for the competition for each of the participating countries based on their final standings
    for country in final_standings:
        index = getIndexByCountryName(countries, country.name)
        countries[index].points[3] = countries[index].points[3] + points_for_competition[final_standings[country] - 1]

def calculateRanking(countries):
    sorted_countries = sorted(countries, key=lambda x: getTotalCountryPoints(x.points), reverse=True)

    for idx, country in enumerate(sorted_countries, start=1):
        country.rank = idx
    
    return sorted_countries