

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