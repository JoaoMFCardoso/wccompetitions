from src.classes.country_class import Country
from src.classes.region_class import Region
from src.classes.season_class import Season
from src.data.input_data import mens_ranking
from src.results_creator import createShortResultsFile, createLongResultsFile, createJSONFile


# Define regions
europe = Region("Europe", 1, 4, 2)
americas = Region("Americas", 2, 2, 1)
asia_pacific = Region("Asia Pacific", 3, 3, 1)
regions = [europe, americas, asia_pacific]

# Get countries from input data
countries = []
for country in mens_ranking:
    country = Country(country["name"], country["region"], country["division"], country["rank"], country["points"])
    countries.append(country)

# Run season simulation
seasons = []
enl_a_eligible_countries = []
pcnl_a_eligible_countries = []

for year in range(10):
    new_season = Season(str(year + 1), regions, countries, enl_a_eligible_countries, pcnl_a_eligible_countries)
    new_season.runSeason()
    seasons.append(new_season)
    countries = new_season.end_countries
    enl_a_eligible_countries = new_season.enl_a_eligible_countries
    pcnl_a_eligible_countries = new_season.pcnl_a_eligible_countries

# Create results file
createShortResultsFile(seasons)
createLongResultsFile(seasons)
#createJSONFile(seasons)