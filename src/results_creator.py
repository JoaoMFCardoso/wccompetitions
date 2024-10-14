import json

def createShortResultsFile(seasons):
    
    # Create the file
    with open('short_simulation_results.txt', 'w') as f:

        # Run all seasons
        for season in seasons:
            f.write(f"\n Year {season.year} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

            f.write(f"\nEuropean Nations League\n")
            f.write(f"A division nations: {season.europe_a_countries}\n")
            f.write(f"B division nations: {season.europe_b_countries}\n")
            f.write(f"C division nations: {season.europe_c_countries}\n")
            f.write(f"D division nations: {season.europe_d_countries}\n")
            f.write(f"\nAmericas Nations League\n")
            f.write(f"A division nations: {season.americas_a_countries}\n")
            f.write(f"B division nations: {season.americas_b_countries}\n")
            f.write(f"\nAsia Pacific Nations League\n")
            f.write(f"A division nations: {season.asia_pacific_a_countries}\n")
            f.write(f"B division nations: {season.asia_pacific_b_countries}\n")
            f.write(f"C division nations: {season.asia_pacific_c_countries}\n")

            #B Division Results
            f.write(f"\nEuropean Nations League B\n")
            f.write(f"  Participating Nations: {len(season.enl_b_results)}\n")
            f.write("   Promoted:\n")
            promotions = season.enl_b_promotions
            for promoted in promotions:
                f.write(f"      {promoted.name}\n")
            f.write("   Relegated:\n")
            relegations = season.enl_b_relegations
            for relegated in relegations:
                f.write(f"      {relegated.name}\n")
            f.write("\n")

            f.write(f"Americas Nations League B\n")
            f.write(f"Participating Nations: {len(season.anl_b_results)}\n")
            f.write("   Promoted:\n")
            promotions = sorted(season.anl_b_results, key=season.anl_b_results.get)[:1]
            for promoted in promotions:
                f.write(f"      {promoted.name}\n")
            f.write("\n")

            f.write(f"Asia Pacific Nations League B\n")
            f.write(f"  Participating Nations: {len(season.apnl_b_results)}\n")
            f.write("   Promoted:\n")
            promotions = season.apnl_b_promotions
            for promoted in promotions:
                f.write(f"      {promoted.name}\n")
            f.write("   Relegated:\n")
            relegations = season.apnl_b_relegations
            for relegated in relegations:
                f.write(f"      {relegated.name}\n")
            f.write("\n")

            #A Division Results
            f.write(f"European Nations League A\n")
            f.write(f"  Participating Nations: {len(season.enl_a_results)}\n")
            winner = season.enl_a_winner[0].name
            f.write(f"  Winner: {winner}\n")
            f.write("\n")

            f.write(f"Pan Continental Nations League A\n")
            f.write(f"  Participating Nations: {len(season.pcnl_a_results)}\n")
            winner = season.pcnl_a_winner[0].name
            f.write(f"  Winner: {winner}\n")
            f.write("\n")

            # World championships results
            f.write(f"World Championships Results *****\n")
            f.write(f"  Participating Nations: {len(season.wc_results)}\n")
            winner = season.wc_winner[0].name
            f.write(f"  Winner: {winner}\n")
            relegations = season.wc_relegations
            f.write("   Relegated:\n")
            for relegated in relegations:
                f.write(f"      {relegated.name}\n")
            f.write("\n")

            #C and D Division Results
            f.write(f"European Nations League C\n")
            f.write(f"  Participating Nations: {len(season.enl_c_results)}\n")
            f.write("   Promoted:\n")
            promotions = season.enl_c_promotions
            for promoted in promotions:
                f.write(f"      {promoted.name}\n")
            f.write("   Relegated:\n")
            relegations = season.enl_c_relegations
            for relegated in relegations:
                f.write(f"      {relegated.name}\n")
            f.write("\n")

            f.write(f"European Nations League D\n")
            f.write(f"  Participating Nations: {len(season.enl_d_results)}\n")
            f.write("   Promoted:\n")
            promotions = season.enl_d_promotions
            for promoted in promotions:
                f.write(f"      {promoted.name}\n")
            f.write("\n")

            f.write(f"Asia Pacific Nations League C\n")
            f.write(f"  Participating Nations: {len(season.apnl_c_results)}\n")
            f.write("   Promoted:\n")
            promotions = season.apnl_c_promotions
            for promoted in promotions:
                f.write(f"      {promoted.name}\n")
            f.write("\n")

    print("results written")

def createLongResultsFile(seasons):
    
    # Create the file
    with open('long_simulation_results.txt', 'w') as f:

        # Run all seasons
        for season in seasons:
            f.write(f"\nYear {season.year}\n")

            f.write(f"\nEuropean Nations League\n")
            f.write(f"A division nations: {season.europe_a_countries}\n")
            f.write(f"B division nations: {season.europe_b_countries}\n")
            f.write(f"C division nations: {season.europe_c_countries}\n")
            f.write(f"D division nations: {season.europe_d_countries}\n")
            f.write(f"\nAmericas Nations League\n")
            f.write(f"A division nations: {season.americas_a_countries}\n")
            f.write(f"B division nations: {season.americas_b_countries}\n")
            f.write(f"\nAsia Pacific Nations League\n")
            f.write(f"A division nations: {season.asia_pacific_a_countries}\n")
            f.write(f"B division nations: {season.asia_pacific_b_countries}\n")
            f.write(f"C division nations: {season.asia_pacific_c_countries}\n")

            #B Division Results
            f.write(f"\nEuropean Nations League B\n")
            f.write(f"Participating Nations: {len(season.enl_b_results)}\n")
            f.write("Promoted:\n")
            promotions = season.enl_b_promotions
            for promoted in promotions:
                f.write(f"{promoted.name}\n")
            f.write("Relegated:\n")
            relegations = season.enl_b_relegations
            for relegated in relegations:
                f.write(f"{relegated.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.enl_b_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            f.write(f"Americas Nations League B\n")
            f.write(f"Participating Nations: {len(season.anl_b_results)}\n")
            f.write("Promoted:\n")
            promotions = sorted(season.anl_b_results, key=season.anl_b_results.get)[:1]
            for promoted in promotions:
                f.write(f"{promoted.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.anl_b_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            f.write(f"Asia Pacific Nations League B\n")
            f.write(f"Participating Nations: {len(season.apnl_b_results)}\n")
            f.write("Promoted:\n")
            promotions = season.apnl_b_promotions
            for promoted in promotions:
                f.write(f"{promoted.name}\n")
            f.write("Relegated:\n")
            relegations = season.apnl_b_relegations
            for relegated in relegations:
                f.write(f"{relegated.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.apnl_b_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            #A Division Results
            f.write(f"European Nations League A\n")
            f.write(f"Participating Nations: {len(season.enl_a_results)}\n")
            winner = season.enl_a_winner[0].name
            f.write(f"Winner: {winner}\n")
            f.write(f"Results:\n")
            for country, rank in season.enl_a_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            f.write(f"Pan Continental Nations League A\n")
            f.write(f"Participating Nations: {len(season.pcnl_a_results)}\n")
            winner = season.pcnl_a_winner[0].name
            f.write(f"Winner: {winner}\n")
            f.write(f"Results:\n")
            for country, rank in season.pcnl_a_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            # World championships results
            f.write(f"World Championships Results\n")
            f.write(f"Participating Nations: {len(season.wc_results)}\n")
            winner = season.wc_winner[0].name
            f.write(f"Winner: {winner}\n")
            relegations = season.wc_relegations
            f.write("Relegated:\n")
            for relegated in relegations:
                f.write(f"{relegated.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.wc_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            #C and D Division Results
            f.write(f"European Nations League C\n")
            f.write(f"Participating Nations: {len(season.enl_c_results)}\n")
            f.write("Promoted:\n")
            promotions = season.enl_c_promotions
            for promoted in promotions:
                f.write(f"{promoted.name}\n")
            f.write("Relegated:\n")
            relegations = season.enl_c_relegations
            for relegated in relegations:
                f.write(f"{relegated.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.enl_c_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            f.write(f"European Nations League D\n")
            f.write(f"Participating Nations: {len(season.enl_d_results)}\n")
            f.write("Promoted:\n")
            promotions = season.enl_d_promotions
            for promoted in promotions:
                f.write(f"{promoted.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.enl_d_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

            f.write(f"Asia Pacific Nations League C\n")
            f.write(f"Participating Nations: {len(season.apnl_c_results)}\n")
            f.write("Promoted:\n")
            promotions = season.apnl_c_promotions
            for promoted in promotions:
                f.write(f"{promoted.name}\n")
            f.write(f"Results:\n")
            for country, rank in season.apnl_c_results.items():
                f.write(f"{rank}-{country.name}\n")
            f.write("\n")

    print("results written")

def createResultsDictionary(results):
    results_dictionary = {}
    for country, rank in results.items():
        results_dictionary[rank] = country.name 
    return results_dictionary

def createJSONFile(seasons):

    # Create the seasons dictionary
    seasons_dictionary = {}
    for season in seasons:
        season_dictionary = {}
        
        # Write year
        season_dictionary["year"] = season.year

        # Write number of nations per division
        nations_dictionary = {}
        european_nations_dictionary = {}
        european_nations_dictionary["A"] = season.europe_a_countries
        european_nations_dictionary["B"] = season.europe_b_countries
        european_nations_dictionary["C"] = season.europe_c_countries
        european_nations_dictionary["D"] = season.europe_d_countries
        nations_dictionary["European Nations League"] = european_nations_dictionary
        americas_nations_dictionary = {}
        americas_nations_dictionary["A"] = season.americas_a_countries
        americas_nations_dictionary["B"] = season.americas_b_countries
        nations_dictionary["Americas Nations League"] = americas_nations_dictionary
        asia_pacific_nations_dictionary = {}
        asia_pacific_nations_dictionary["A"] = season.asia_pacific_a_countries
        asia_pacific_nations_dictionary["B"] = season.asia_pacific_b_countries
        asia_pacific_nations_dictionary["C"] = season.asia_pacific_c_countries
        nations_dictionary["Asia Pacific Nations League"] = asia_pacific_nations_dictionary
        
        # Division results
        competitions_dictionary = {}

        # B division
        enl_b_dictionary = {}
        enl_b_dictionary["competition"] = "European Nations League B"
        enl_b_dictionary["region"] = 1
        enl_b_dictionary["division"] = 2
        enl_b_dictionary["field"] = len(season.enl_b_results)
        enl_b_promoted_list = []
        promotions = season.enl_b_promotions
        for promoted in promotions:
            enl_b_promoted_list.append(promoted.name) 
        enl_b_dictionary["promotions"] = len(enl_b_promoted_list)
        enl_b_dictionary["promoted countries"] = enl_b_promoted_list
        enl_b_relegated_list = []
        relegations = season.enl_b_relegations
        for relegated in relegations:
            enl_b_relegated_list.append(relegated.name) 
        enl_b_dictionary["relegations"] = len(enl_b_relegated_list)
        enl_b_dictionary["relegated countries"] = enl_b_relegated_list
        enl_b_dictionary["results"] = createResultsDictionary(season.enl_b_results)
        competitions_dictionary["1B"] = enl_b_dictionary

        anl_b_dictionary = {}
        anl_b_dictionary["competition"] = "Americas Nations League B"
        anl_b_dictionary["region"] = 2
        anl_b_dictionary["division"] = 2
        anl_b_dictionary["field"] = len(season.anl_b_results)
        anl_b_promoted_list = []
        promotions = season.anl_b_promotions
        for promoted in promotions:
            anl_b_promoted_list.append(promoted.name) 
        anl_b_dictionary["promotions"] = len(anl_b_promoted_list)
        anl_b_dictionary["promoted countries"] = anl_b_promoted_list
        anl_b_dictionary["results"] = createResultsDictionary(season.anl_b_results)
        competitions_dictionary["2B"] = anl_b_dictionary

        apnl_b_dictionary = {}
        apnl_b_dictionary["competition"] = "Asia Pacific Nations League B"
        apnl_b_dictionary["region"] = 3
        apnl_b_dictionary["division"] = 2
        apnl_b_dictionary["field"] = len(season.apnl_b_results)
        apnl_b_promoted_list = []
        promotions = season.apnl_b_promotions
        for promoted in promotions:
            apnl_b_promoted_list.append(promoted.name) 
        apnl_b_dictionary["promotions"] = len(apnl_b_promoted_list)
        apnl_b_dictionary["promoted countries"] = apnl_b_promoted_list
        apnl_b_relegated_list = []
        relegations = season.apnl_b_relegations
        for relegated in relegations:
            apnl_b_relegated_list.append(relegated.name) 
        apnl_b_dictionary["relegations"] = len(apnl_b_relegated_list)
        apnl_b_dictionary["relegated countries"] = apnl_b_relegated_list 
        apnl_b_dictionary["results"] = createResultsDictionary(season.apnl_b_results)
        competitions_dictionary["3B"] = apnl_b_dictionary

        # A division
        enl_a_dictionary = {}
        enl_a_dictionary["competition"] = "European Nations League A"
        enl_a_dictionary["region"] = 1
        enl_a_dictionary["division"] = 1
        enl_a_dictionary["field"] = len(season.enl_a_results)
        enl_a_dictionary["winner"] = season.enl_a_winner[0].name
        enl_a_dictionary["results"] = createResultsDictionary(season.enl_a_results)
        competitions_dictionary["1A"] = enl_a_dictionary

        pcnl_a_dictionary = {}
        pcnl_a_dictionary["competition"] = "Pan Continental Nations League A"
        pcnl_a_dictionary["region"] = [2, 3]
        pcnl_a_dictionary["division"] = 1
        pcnl_a_dictionary["field"] = len(season.pcnl_a_results)
        pcnl_a_dictionary["winner"] = season.pcnl_a_winner[0].name
        pcnl_a_dictionary["results"] = createResultsDictionary(season.pcnl_a_results)
        competitions_dictionary["23A"] = pcnl_a_dictionary

        # World Championships
        wc_dictionary = {}
        wc_dictionary["competition"] = "World Championships"
        wc_dictionary["region"] = [1, 2, 3]
        wc_dictionary["division"] = 1
        wc_dictionary["field"] = len(season.wc_results)
        wc_dictionary["winner"] = season.wc_winner[0].name
        wc_relegated_list = []
        relegations = season.wc_relegations
        for relegated in relegations:
            wc_relegated_list.append(relegated.name) 
        wc_dictionary["relegations"] = len(wc_relegated_list)
        wc_dictionary["relegated countries"] = wc_relegated_list
        wc_dictionary["results"] = createResultsDictionary(season.wc_results)
        competitions_dictionary["WC"] = wc_dictionary

        # C division
        enl_c_dictionary = {}
        enl_c_dictionary["competition"] = "European Nations League C"
        enl_c_dictionary["region"] = 1
        enl_c_dictionary["division"] = 3
        enl_c_dictionary["field"] = len(season.enl_c_results)
        enl_c_promoted_list = []
        promotions = season.enl_c_promotions
        for promoted in promotions:
            enl_c_promoted_list.append(promoted.name) 
        enl_c_dictionary["promotions"] = len(enl_c_promoted_list)
        enl_c_dictionary["promoted countries"] = enl_c_promoted_list
        enl_c_relegated_list = []
        relegations = season.enl_c_relegations
        for relegated in relegations:
            enl_c_relegated_list.append(relegated.name) 
        enl_c_dictionary["relegations"] = len(enl_c_relegated_list)
        enl_c_dictionary["relegated countries"] = enl_c_relegated_list
        enl_c_dictionary["results"] = createResultsDictionary(season.enl_c_results)
        competitions_dictionary["1C"] = enl_c_dictionary

        apnl_c_dictionary = {}
        apnl_c_dictionary["competition"] = "Asia Pacific Nations League C"
        apnl_c_dictionary["region"] = 3
        apnl_c_dictionary["division"] = 3
        apnl_c_dictionary["field"] = len(season.apnl_c_results)
        apnl_c_promoted_list = []
        promotions = season.apnl_c_promotions
        for promoted in promotions:
            apnl_c_promoted_list.append(promoted.name) 
        apnl_c_dictionary["promotions"] = len(apnl_c_promoted_list)
        apnl_c_dictionary["promoted countries"] = apnl_c_promoted_list
        apnl_c_dictionary["results"] = createResultsDictionary(season.apnl_c_results)
        competitions_dictionary["3C"] = apnl_c_dictionary

        # D division
        enl_d_dictionary = {}
        enl_d_dictionary["competition"] = "European Nations League D"
        enl_d_dictionary["region"] = 1
        enl_d_dictionary["division"] = 4
        enl_d_dictionary["field"] = len(season.enl_d_results)
        enl_d_promoted_list = []
        promotions = season.enl_d_promotions
        for promoted in promotions:
            enl_d_promoted_list.append(promoted.name) 
        enl_d_dictionary["promotions"] = len(enl_d_promoted_list)
        enl_d_dictionary["promoted countries"] = enl_d_promoted_list
        enl_d_dictionary["results"] = createResultsDictionary(season.enl_d_results)
        competitions_dictionary["1D"] = enl_d_dictionary

        season_dictionary["competitions"] = competitions_dictionary
        seasons_dictionary[season.year] = season_dictionary

    # Write the data to a JSON file
    with open("long_results.json", "w") as json_file:
        json.dump(seasons_dictionary, json_file, indent=4)