from src.competition_classes import Competition, printResults, promoteCountry, relegateCountry, countCountriesInDivisionRegion, countriesPerRegion

class Season:
    def __init__(self, year, regions_list, start_countries, enl_a_eligible_countries, pcnl_a_eligible_countries):
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
        self.enl_a_eligible_countries = enl_a_eligible_countries
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
        self.pcnl_a_eligible_countries = pcnl_a_eligible_countries
        self.anl_b_results = []
        self.anl_b_promotions = []
        self.apnl_b_results = []
        self.apnl_b_promotions = []
        self.apnl_b_relegations = []
        self.apnl_c_results = []
        self.apnl_c_promotions = []


    def runSeason(self):
        
        season_name = self.year
        new_countries = self.start_countries
        
        self.europe_a_countries = countCountriesInDivisionRegion(self.start_countries, 1, 1)
        self.europe_b_countries = countCountriesInDivisionRegion(self.start_countries, 2, 1)
        self.europe_c_countries = countCountriesInDivisionRegion(self.start_countries, 3, 1)
        self.europe_d_countries = countCountriesInDivisionRegion(self.start_countries, 4, 1)
        self.americas_a_countries = countCountriesInDivisionRegion(self.start_countries, 1, 2)
        self.americas_b_countries = countCountriesInDivisionRegion(self.start_countries, 2, 2)
        self.asia_pacific_a_countries = countCountriesInDivisionRegion(self.start_countries, 1, 3)
        self.asia_pacific_b_countries = countCountriesInDivisionRegion(self.start_countries, 2, 3)
        self.asia_pacific_c_countries = countCountriesInDivisionRegion(self.start_countries, 3, 3)

        # Running competitions to gather promoted countries for World Championships
        # B divisions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Dynamic Relegations
        # Calculate the number of relegations per B (and C) division by the number of nations in the worlds
        # The formula is:
        # min(<region nations in worlds> , <worlds relegations>)
        relegations_enl_b = min((self.europe_a_countries + self.regions_list[0].promotion_spots), len(self.wc_relegations))
        relegations_apnl_b = min((self.asia_pacific_a_countries + self.regions_list[2].promotion_spots), len(self.wc_relegations))

        # European Nations League Division B
        enl_b = Competition("European Nations League B", 1, 2, 2, relegations_enl_b, 10)
        enl_b.runCompetition(self.start_countries, [])
        self.enl_b_results = enl_b.final_rankings
        self.enl_b_promotions = enl_b.promoted_countries
        self.enl_b_relegations = enl_b.relegated_countries
        self.enl_a_eligible_countries = enl_b.eligible_countries
        
        # Americas Nations League Division B
        anl_b = Competition("Americas Nations League B", 2, 2, 1, 0, 4)
        anl_b.runCompetition(self.start_countries, [])
        self.anl_b_results = anl_b.final_rankings
        self.anl_b_promotions = anl_b.promoted_countries

        # Asia Pacific Nations League Division B
        apnl_b = Competition("Asia Pacific Nations League B", 3, 2, 1, relegations_apnl_b, 4)
        apnl_b.runCompetition(self.start_countries, [])
        self.apnl_b_results = apnl_b.final_rankings
        self.apnl_b_promotions = apnl_b.promoted_countries
        self.apnl_b_relegations = apnl_b.relegated_countries

        # Create combined eligible countries for pcnl based on the existing order of the provided lists
        self.pcnl_a_eligible_countries = [item for pair in zip(anl_b.eligible_countries, apnl_b.eligible_countries) for item in pair]

        # A divisions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # European Nations League Division A
        enl_a = Competition("European Nations League A", 1, 1, 1, 0, 0)
        enl_a.runCompetition(self.start_countries, self.enl_a_eligible_countries)
        self.enl_a_results = enl_a.final_rankings
        self.enl_a_winner = enl_a.promoted_countries
        
        # Pan Continental Nations League Division A
        pcnl_a = Competition("Pan Continental Nations League A", 2, 1, 1, 0, 0)
        pcnl_a.runCompetition(self.start_countries, self.pcnl_a_eligible_countries)
        self.pcnl_a_results = pcnl_a.final_rankings
        self.pcnl_a_winner = pcnl_a.promoted_countries

        #Promote countries from the B's in preparation for the world championships
        promoteCountry(enl_b.promoted_countries, new_countries)
        promoteCountry(anl_b.promoted_countries, new_countries)
        promoteCountry(apnl_b.promoted_countries, new_countries)
        
        # World Championships >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Run World Championships
        world_championships = Competition("World Championships", 0, 1, 1, 4, 0)
        world_championships.runCompetition(new_countries, [])
        self.wc_results = world_championships.final_rankings
        self.wc_winner = world_championships.promoted_countries
        self.wc_relegations = world_championships.relegated_countries
        
        # C and D divisions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Dynamic Promotions and Relegations
        # Calculate the number of promotions for the C divisions
        # The formula is:
        # <promotions per region> + <number of relegated countries from B> - <number of relegated countries of the region from worlds>
        wc_relegations_per_region = countriesPerRegion(world_championships.relegated_countries)
        promotions_enl_c = self.regions_list[0].promotion_spots + len(enl_b.relegated_countries) - wc_relegations_per_region[1]
        promotions_apnl_c = self.regions_list[2].promotion_spots + len(apnl_b.relegated_countries) - wc_relegations_per_region[3]

        # Calculate the number of relegations for the C divisions
        # The formula is:
        # max(<region nations relegated from worlds>, <number of promotion spots in D division>)
        relegations_enl_c = max(wc_relegations_per_region[1], 2)

        # Calculate the number of promotions for the D division
        # The formula is:
        # <starting number of countries in C> - <number of relegated countries in B> + <teams remaining in C after promotion/relegation>
        # <teams remaining in C after promotion/relegation> = 12 - <promotion from C to B> - <relegation from C to D>
        enl_c_remaining_teams_after_prorel = 12 - promotions_enl_c - relegations_enl_c
        enl_c_number_of_starting_countries = countCountriesInDivisionRegion(new_countries, 3, 1)
        promotions_enl_d = enl_c_number_of_starting_countries - relegations_enl_b + enl_c_remaining_teams_after_prorel

        # European Nations League Division C
        enl_c = Competition("European Nations League C", 1, 3, promotions_enl_c, relegations_enl_c, 0)
        enl_c.runCompetition(self.start_countries, [])
        self.enl_c_results = enl_c.final_rankings
        self.enl_c_promotions = enl_c.promoted_countries
        self.enl_c_relegations = enl_c.relegated_countries

        # European Nations League Division D
        enl_d = Competition("European Nations League D", 1, 4, promotions_enl_d, 0, 0)
        enl_d.runCompetition(self.start_countries, [])
        self.enl_d_results = enl_d.final_rankings
        self.enl_d_promotions = enl_d.promoted_countries
        
        # Asia Pacific Nations League Division C
        apnl_c = Competition("Asia Pacific Nations League C", 3, 3, promotions_apnl_c, 0, 0)
        apnl_c.runCompetition(self.start_countries, [])
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
        
        self.end_countries = new_countries