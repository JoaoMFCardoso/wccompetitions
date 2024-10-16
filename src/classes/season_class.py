import copy
from src.classes.competition_class import Competition 
from src.ranking_calculator import preparePointsForCalculation, calculatePointsForCompetition, calculateRanking
from src.utilities import printResults, promoteCountry, relegateCountry, countCountriesInDivisionRegion, countriesPerRegion

class Season:
    def __init__(self, year, regions_list, start_countries, enl_a_wildcard_eligible_countries, pcnl_a_wildcard_eligible_countries):
        self.year = year
        self.regions_list = regions_list
        self.start_countries = start_countries
        self.end_countries = []
        self.europe_a_countries = 0
        self.europe_b_countries = 0
        self.europe_c_countries = 0
        self.europe_d_countries = 0
        self.americas_a_countries = 0
        self.americas_b_countries = 0
        self.asia_pacific_a_countries = 0
        self.asia_pacific_b_countries = 0
        self.asia_pacific_c_countries = 0
        self.wc_results = []
        self.wc_winner = []
        self.wc_relegations = [0,0,0,0]
        self.enl_a_results = []
        self.enl_a_winner = []
        self.enl_a_wildcard_eligible_countries = enl_a_wildcard_eligible_countries
        self.enl_b_results = []
        self.enl_b_promotions = []
        self.enl_b_relegations = []
        self.enl_c_results = []
        self.enl_c_promotions = []
        self.enl_c_relegations = []
        self.enl_d_results = []
        self.enl_d_promotions = []
        self.pcnl_a_results = []
        self.pcnl_a_winner = []
        self.pcnl_a_wildcard_eligible_countries = pcnl_a_wildcard_eligible_countries
        self.anl_b_results = []
        self.anl_b_promotions = []
        self.apnl_b_results = []
        self.apnl_b_promotions = []
        self.apnl_b_relegations = []
        self.apnl_c_results = []
        self.apnl_c_promotions = []


    def runSeason(self):
        new_countries = copy.deepcopy(self.start_countries)
        
        self.europe_a_countries = countCountriesInDivisionRegion(new_countries, 1, 1)
        self.europe_b_countries = countCountriesInDivisionRegion(new_countries, 2, 1)
        self.europe_c_countries = countCountriesInDivisionRegion(new_countries, 3, 1)
        self.europe_d_countries = countCountriesInDivisionRegion(new_countries, 4, 1)
        self.americas_a_countries = countCountriesInDivisionRegion(new_countries, 1, 2)
        self.americas_b_countries = countCountriesInDivisionRegion(new_countries, 2, 2)
        self.asia_pacific_a_countries = countCountriesInDivisionRegion(new_countries, 1, 3)
        self.asia_pacific_b_countries = countCountriesInDivisionRegion(new_countries, 2, 3)
        self.asia_pacific_c_countries = countCountriesInDivisionRegion(new_countries, 3, 3)

        # Create all competitions
        # With some placeholders '0' for relegations and promotions
        # Reminder of the input arguments:
        # competition name
        # competition region
        # competition division
        # competition field size
        # competition minimum number of promotions
        # competition number of promotions
        # competition minimum number of relegations
        # competition number of relegations
        # competition number of eligible for invites to be created from this competition
        enl_b = Competition("European Nations League B", 1, 2, 12, 2, 2, 2, 0, 10)
        anl_b = Competition("Americas Nations League B", 2, 2, 8, 1, 1, 0, 0, 4)
        apnl_b = Competition("Asia Pacific Nations League B", 3, 2, 8, 1, 1, 1, 0, 4)
        enl_a = Competition("European Nations League A", 1, 1, 10, 1, 1, 0, 0, 0)
        pcnl_a = Competition("Pan Continental Nations League A", 2, 1, 8, 1, 1, 0, 0, 0)
        world_championships = Competition("World Championships", 0, 1, 16, 1, 1, 4, 4, 0)
        enl_c = Competition("European Nations League C", 1, 3, 12, 2, 0, 2, 0, 0)
        enl_d = Competition("European Nations League D", 1, 4, 12, 2, 0, 0, 0, 0)
        apnl_c = Competition("Asia Pacific Nations League C", 3, 3, 8, 1, 0, 0, 0, 0)

        # Running competitions to gather promoted countries for World Championships
        # B divisions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Dynamic Relegations
        # Calculate the number of relegations per B (and C) division by the number of nations in the worlds
        # The formula is:
        # min(<region nations in worlds> , <worlds relegations>)
        relegations_enl_b = min((self.europe_a_countries + self.regions_list[0].promotion_spots), len(self.wc_relegations))
        relegations_apnl_b = min((self.asia_pacific_a_countries + self.regions_list[2].promotion_spots), len(self.wc_relegations))

        # European Nations League Division B
        enl_b.number_of_relegations = relegations_enl_b
        enl_b.runCompetition(new_countries, [])
        self.enl_b_results = enl_b.final_rankings
        self.enl_b_promotions = enl_b.promoted_countries
        self.enl_b_relegations = enl_b.relegated_countries
        self.enl_a_wildcard_eligible_countries = enl_b.wildcard_eligible_countries
        
        # Americas Nations League Division B
        anl_b.runCompetition(new_countries, [])
        self.anl_b_results = anl_b.final_rankings
        self.anl_b_promotions = anl_b.promoted_countries

        # Asia Pacific Nations League Division B
        apnl_b.number_of_relegations = relegations_apnl_b
        apnl_b.runCompetition(new_countries, [])
        self.apnl_b_results = apnl_b.final_rankings
        self.apnl_b_promotions = apnl_b.promoted_countries
        self.apnl_b_relegations = apnl_b.relegated_countries

        # Create combined eligible countries for pcnl based on the existing order of the provided lists
        self.pcnl_a_wildcard_eligible_countries = [item for pair in zip(anl_b.wildcard_eligible_countries, apnl_b.wildcard_eligible_countries) for item in pair]

        # A divisions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # European Nations League Division A
        enl_a.runCompetition(new_countries, self.enl_a_wildcard_eligible_countries)
        self.enl_a_results = enl_a.final_rankings
        self.enl_a_winner = enl_a.promoted_countries
        
        # Pan Continental Nations League Division A
        pcnl_a.runCompetition(new_countries, self.pcnl_a_wildcard_eligible_countries)
        self.pcnl_a_results = pcnl_a.final_rankings
        self.pcnl_a_winner = pcnl_a.promoted_countries

        #Promote countries from the B's in preparation for the world championships
        promoteCountry(enl_b.promoted_countries, new_countries)
        promoteCountry(anl_b.promoted_countries, new_countries)
        promoteCountry(apnl_b.promoted_countries, new_countries)
        
        # World Championships >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Run World Championships
        world_championships.runCompetition(new_countries, [])
        self.wc_results = world_championships.final_rankings
        self.wc_winner = world_championships.promoted_countries
        self.wc_relegations = world_championships.relegated_countries
        
        # C and D divisions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Dynamic Promotions and Relegations
        # Calculate the number of promotions for the C divisions
        # The formula is:
        # (<promotions from B division> + <relegations from B division>) - <number of relegations from region at worlds>
        wc_relegations_per_region = countriesPerRegion(world_championships.relegated_countries)
        promotions_enl_c = (enl_b.number_of_promotions + enl_b.number_of_relegations) -  wc_relegations_per_region[1] 
        promotions_apnl_c = (apnl_b.number_of_promotions + apnl_b.number_of_relegations) -  wc_relegations_per_region[3] 

        # Calculate the number of relegations for the C divisions
        # The formula is:
        # max(<region nations relegated from worlds>, <number of minimum relegations from C division>)
        relegations_enl_c = max(wc_relegations_per_region[1], enl_c.min_number_of_relegations)

        # Calculate the number of promotions for the D division
        # The formula is:
        # <promotions in division C> + <relegations in division C> - <relegations in division B>
        promotions_enl_d = promotions_enl_c + relegations_enl_c - relegations_enl_b

        # European Nations League Division C
        enl_c.number_of_promotions = promotions_enl_c
        enl_c.number_of_relegations = relegations_enl_c
        enl_c.runCompetition(new_countries, [])
        self.enl_c_results = enl_c.final_rankings
        self.enl_c_promotions = enl_c.promoted_countries
        self.enl_c_relegations = enl_c.relegated_countries

        # European Nations League Division D
        enl_d.number_of_promotions = promotions_enl_d
        enl_d.runCompetition(new_countries, [])
        self.enl_d_results = enl_d.final_rankings
        self.enl_d_promotions = enl_d.promoted_countries
        
        # Asia Pacific Nations League Division C
        apnl_c.number_of_promotions = promotions_apnl_c
        apnl_c.runCompetition(new_countries, [])
        self.apnl_c_results = apnl_c.final_rankings
        self.apnl_c_promotions = apnl_c.promoted_countries

        #Promote countries in C and D, and relegate all countries for new season
        relegateCountry(world_championships.relegated_countries, new_countries)
        relegateCountry(enl_b.relegated_countries, new_countries)
        relegateCountry(apnl_b.relegated_countries, new_countries)
        promoteCountry(enl_c.promoted_countries, new_countries)
        relegateCountry(enl_c.relegated_countries, new_countries)
        promoteCountry(enl_d.promoted_countries, new_countries)
        promoteCountry(apnl_c.promoted_countries, new_countries)
        
        # Calculate points per competition
        preparePointsForCalculation(new_countries)
        calculatePointsForCompetition(new_countries,"World Championships", world_championships.final_rankings)
        calculatePointsForCompetition(new_countries,"European Nations League A", enl_a.final_rankings)
        calculatePointsForCompetition(new_countries,"European Nations League B", enl_b.final_rankings)
        calculatePointsForCompetition(new_countries,"European Nations League C", enl_c.final_rankings)
        calculatePointsForCompetition(new_countries,"European Nations League D", enl_d.final_rankings)
        calculatePointsForCompetition(new_countries,"Pan Continental Nations League A", pcnl_a.final_rankings)
        calculatePointsForCompetition(new_countries,"Americas Nations League B", anl_b.final_rankings)
        calculatePointsForCompetition(new_countries,"Asia Pacific Nations League B", apnl_b.final_rankings)
        calculatePointsForCompetition(new_countries,"Asia Pacific Nations League C", apnl_c.final_rankings)

        # Calculate country ranking
        new_countries = calculateRanking(new_countries)

        self.end_countries = copy.deepcopy(new_countries)