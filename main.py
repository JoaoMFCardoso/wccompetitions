from src.competition_classes import Region, Country
from src.season_classes import Season
from src.results_creator import createShortResultsFile, createLongResultsFile, createJSONFile


# Define regions
europe = Region("Europe", 1, 4, 2)
americas = Region("Americas", 2, 2, 1)
asia_pacific = Region("Asia Pacific", 3, 3, 1)
regions = [europe, americas, asia_pacific]

# Define countries data (starting conditions)
data = [
    ["Canada", 2, 1],
    ["Korea", 3, 1, ],
    ["USA", 2, 1],
    ["Japan", 3, 1],
    ["Philippines", 3, 2],
    ["Chinese Taipei", 3, 2],
    ["Kazakhstan", 3, 2],
    ["Hong Kong", 3, 2],
    ["New Zealand", 3, 2],
    ["India", 3, 2],
    ["Saudi Arabia", 3, 2],
    ["China", 3, 2],
    ["Qatar", 3, 2],
    ["Kyrgystan", 3, 2],
    ["Australia", 3, 2],
    ["Nigeria", 3, 2],
    ["Turkmenistan", 3, 3],
    ["Kuwait", 3, 3],
    ["Thailand", 3, 3],
    ["Mongolia", 3, 3],
    ["Pakistan", 3, 3],
    ["Afghanistan", 3, 3],
    ["Kenya", 3, 3],
    ["US Virgin Islands", 2, 2],
    ["Dominican Republic", 2, 2],
    ["Puerto Rico", 2, 2],
    ["Mexico", 2, 2],
    ["Jamaica", 2, 2],
    ["Bolivia", 2, 2],
    ["Guyana", 2, 2],
    ["Brazil", 2, 2],
    ["Switzerland", 1, 1],
    ["Norway", 1, 1],
    ["Türkiye", 1, 1],
    ["Germany", 1, 1],
    ["Sweden", 1, 1],
    ["Scotland", 1, 1],
    ["Italy", 1, 1],
    ["Czechia", 1, 1],
    ["Finland", 1, 2],
    ["Austria", 1, 2],
    ["Estonia", 1, 2],
    ["Slovakia", 1, 2],
    ["Denmark", 1, 2],
    ["Latvia", 1, 2],
    ["Netherlands", 1, 2],
    ["Hungary", 1, 2],
    ["Belgium", 1, 2],
    ["England", 1, 2],
    ["Spain", 1, 2],
    ["Wales", 1, 2],
    ["Poland", 1, 3],
    ["Romania", 1, 3],
    ["Liechtenstein", 1, 3],
    ["Lithuania", 1, 3],
    ["Andorra", 1, 3],
    ["Ukraine", 1, 3],
    ["France", 1, 3],
    ["Bulgaria", 1, 3],
    ["Portugal", 1, 3],
    ["Slovenia", 1, 3],
    ["Croatia", 1, 3],
    ["Ireland", 1, 3],
    ["Monaco", 1, 4],
    ["Bosnia & Herzegovina", 1, 4],
    ["Iceland", 1, 4],
    ["Greece", 1, 4],
    ["Georgia", 1, 4],
    ["Israel", 1, 4],
    ["Kosovo", 1, 4],
    ["Serbia", 1, 4],
    ["Luxembourg", 1, 4]
]

# Convert country data into Country objects
countries = []
for item in data:
    country = Country(item[0], item[1], item[2])
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
createJSONFile(seasons)