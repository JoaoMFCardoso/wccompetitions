weight_for_ranking = 1.0
weight_for_points = 1.0
weight_for_season_points = [0.25, 0.5, 0.75, 1.0]

competition_points_multiplier = {
    "World Championships": 7,
    "European Nations League A": 5,
    "Pan Continental Nations League A": 5,
    "European Nations League B": 3,
    "Americas Nations League B": 3,
    "Asia Pacific Nations League B": 3,
    "European Nations League C": 2,
    "Asia Pacific Nations League C": 2,
    "European Nations League D": 1
}

competition_points = {
        1: 240.0,
        2: 200.0,
        3: 180.0,
        4: 150.0,
        5: 120.0,
        6: 110.0,
        7: 100.0,
        8: 90.0,
        9: 80.0,
        10: 70.0,
        11: 60.0,
        12: 50.0,
        13: 40.0,
        14: 30.0,
        15: 20.0,
        16: 10.0
}

mens_ranking = [
    {
        "name": "Sweden",
        "region": 1,
        "division": 1,
        "rank": 1,
        "points": [0.0, 0.0, 0.0, 84.085]
    },
    {
        "name": "Canada",
        "region": 2,
        "division": 1,
        "rank": 2,
        "points": [0.0, 0.0, 0.0, 78.085]
    },
    {
        "name": "Scotland",
        "region": 1,
        "division": 1,
        "rank": 3,
        "points": [0.0, 0.0, 0.0, 60.845]
    },
    {
        "name": "Italy",
        "region": 1,
        "division": 1,
        "rank": 4,
        "points": [0.0, 0.0, 0.0, 48.577]
    },
    {
        "name": "Switzerland",
        "region": 1,
        "division": 1,
        "rank": 5,
        "points": [0.0, 0.0, 0.0, 45.085]
    },
    {
        "name": "United States of America",
        "region": 2,
        "division": 1,
        "rank": 6,
        "points": [0.0, 0.0, 0.0, 38.296]
    },
    {
        "name": "Korea",
        "region": 3,
        "division": 1,
        "rank": 7,
        "points": [0.0, 0.0, 0.0, 34.507]
    },
    {
        "name": "Norway",
        "region": 1,
        "division": 1,
        "rank": 8,
        "points": [0.0, 0.0, 0.0, 26.282]
    },
    {
        "name": "Germany",
        "region": 1,
        "division": 1,
        "rank": 9,
        "points": [0.0, 0.0, 0.0, 25.690]
    },
    {
        "name": "Japan",
        "region": 3,
        "division": 1,
        "rank": 10,
        "points": [0.0, 0.0, 0.0, 19.831]
    },
    {
        "name": "Czechia",
        "region": 1,
        "division": 1,
        "rank": 11,
        "points": [0.0, 0.0, 0.0, 19.324]
    },
    {
        "name": "Netherlands",
        "region": 1,
        "division": 1,
        "rank": 12,
        "points": [0.0, 0.0, 0.0, 16.535]
    },
    {
        "name": "Russia",
        "region": 1,
        "division": 4,
        "rank": 13,
        "points": [0.0, 0.0, 0.0, 12.225]
    },
    {
        "name": "Denmark",
        "region": 1,
        "division": 2,
        "rank": 14,
        "points": [0.0, 0.0, 0.0, 11.901]
    },
    {
        "name": "Finland",
        "region": 1,
        "division": 2,
        "rank": 15,
        "points": [0.0, 0.0, 0.0, 11.873]
    },
    {
        "name": "Türkiye",
        "region": 1,
        "division": 2,
        "rank": 16,
        "points": [0.0, 0.0, 0.0, 11.718]
    },
    {
        "name": "China",
        "region": 3,
        "division": 2,
        "rank": 17,
        "points": [0.0, 0.0, 0.0, 9.803]
    },
    {
        "name": "Spain",
        "region": 1,
        "division": 2,
        "rank": 18,
        "points": [0.0, 0.0, 0.0, 8.659]
    },
    {
        "name": "New Zealand",
        "region": 3,
        "division": 2,
        "rank": 2,
        "points": [0.0, 0.0, 0.0, 48.577]
    },
    {
        "name": "Chinese Taipei",
        "region": 3,
        "division": 2,
        "rank": 19,
        "points": [0.0, 0.0, 0.0, 8.141]
    },
    {
        "name": "Latvia",
        "region": 1,
        "division": 2,
        "rank": 19,
        "points": [0.0, 0.0, 0.0, 8.141]
    },
    {
        "name": "Austria",
        "region": 1,
        "division": 2,
        "rank": 22,
        "points": [0.0, 0.0, 0.0, 6.792]
    },
    {
        "name": "England",
        "region": 1,
        "division": 2,
        "rank": 23,
        "points": [0.0, 0.0, 0.0, 6.738]
    },
    {
        "name": "Australia",
        "region": 3,
        "division": 2,
        "rank": 24,
        "points": [0.0, 0.0, 0.0, 5.555]
    },
    {
        "name": "Belgium",
        "region": 1,
        "division": 2,
        "rank": 25,
        "points": [0.0, 0.0, 0.0, 5.392]
    },
    {
        "name": "Slovakia",
        "region": 1,
        "division": 2,
        "rank": 26,
        "points": [0.0, 0.0, 0.0, 5.192]
    },
    {
        "name": "Wales",
        "region": 1,
        "division": 2,
        "rank": 27,
        "points": [0.0, 0.0, 0.0, 4.921]
    },
    {
        "name": "Hungary",
        "region": 1,
        "division": 2,
        "rank": 28,
        "points": [0.0, 0.0, 0.0, 4.837]
    },
    {
        "name": "Estonia",
        "region": 1,
        "division": 3,
        "rank": 29,
        "points": [0.0, 0.0, 0.0, 4.679]
    },
    {
        "name": "France",
        "region": 1,
        "division": 2,
        "rank": 30,
        "points": [0.0, 0.0, 0.0, 3.786]
    },
    {
        "name": "Slovenia",
        "region": 1,
        "division": 3,
        "rank": 31,
        "points": [0.0, 0.0, 0.0, 3.550]
    },
    {
        "name": "Ireland",
        "region": 1,
        "division": 3,
        "rank": 32,
        "points": [0.0, 0.0, 0.0, 3.468]
    },
    {
        "name": "Brazil",
        "region": 2,
        "division": 2,
        "rank": 33,
        "points": [0.0, 0.0, 0.0, 3.366]
    },
    {
        "name": "Guyana",
        "region": 2,
        "division": 2,
        "rank": 34,
        "points": [0.0, 0.0, 0.0, 3.099]
    },
    {
        "name": "Kazakhstan",
        "region": 3,
        "division": 2,
        "rank": 35,
        "points": [0.0, 0.0, 0.0, 2.890]
    },
    {
        "name": "Hong Kong",
        "region": 3,
        "division": 2,
        "rank": 36,
        "points": [0.0, 0.0, 0.0, 2.766]
    },
    {
        "name": "Ukraine",
        "region": 1,
        "division": 3,
        "rank": 37,
        "points": [0.0, 0.0, 0.0, 2.665]
    },
    {
        "name": "Poland",
        "region": 1,
        "division": 3,
        "rank": 38,
        "points": [0.0, 0.0, 0.0, 2.592]
    },
    {
        "name": "Romania",
        "region": 1,
        "division": 3,
        "rank": 39,
        "points": [0.0, 0.0, 0.0, 2.361]
    },
    {
        "name": "Liechtenstein",
        "region": 1,
        "division": 3,
        "rank": 40,
        "points": [0.0, 0.0, 0.0, 2.132]
    },
    {
        "name": "Croatia",
        "region": 1,
        "division": 3,
        "rank": 41,
        "points": [0.0, 0.0, 0.0, 2.045]
    },
    {
        "name": "Portugal",
        "region": 1,
        "division": 3,
        "rank": 42,
        "points": [0.0, 0.0, 0.0, 1.972]
    },
    {
        "name": "Lithuania",
        "region": 1,
        "division": 3,
        "rank": 43,
        "points": [0.0, 0.0, 0.0, 1.848]
    },
    {
        "name": "India",
        "region": 3,
        "division": 2,
        "rank": 44,
        "points": [0.0, 0.0, 0.0, 1.746]
    },
    {
        "name": "Mexico",
        "region": 2,
        "division": 2,
        "rank": 45,
        "points": [0.0, 0.0, 0.0, 1.701]
    },
    {
        "name": "Andorra",
        "region": 1,
        "division": 3,
        "rank": 46,
        "points": [0.0, 0.0, 0.0, 1.701]
    },
    {
        "name": "Bulgaria",
        "region": 1,
        "division": 3,
        "rank": 47,
        "points": [0.0, 0.0, 0.0, 1.699]
    },
    {
        "name": "Belarus",
        "region": 1,
        "division": 4,
        "rank": 48,
        "points": [0.0, 0.0, 0.0, 1.623]
    },
    {
        "name": "Qatar",
        "region": 3,
        "division": 2,
        "rank": 49,
        "points": [0.0, 0.0, 0.0, 1.611]
    },
    {
        "name": "Nigeria",
        "region": 3,
        "division": 2,
        "rank": 50,
        "points": [0.0, 0.0, 0.0, 1.409]
    },
    {
        "name": "Phillipines",
        "region": 3,
        "division": 2,
        "rank": 51,
        "points": [0.0, 0.0, 0.0, 1.352]
    },
    {
        "name": "Kyrgyzstan",
        "region": 3,
        "division": 2,
        "rank": 52,
        "points": [0.0, 0.0, 0.0, 1.318]
    },
    {
        "name": "Saudi Arabia",
        "region": 3,
        "division": 2,
        "rank": 53,
        "points": [0.0, 0.0, 0.0, 1.304]
    },
    {
        "name": "Greece",
        "region": 1,
        "division": 4,
        "rank": 54,
        "points": [0.0, 0.0, 0.0, 0.946]
    },
    {
        "name": "Kenya",
        "region": 3,
        "division": 3,
        "rank": 55,
        "points": [0.0, 0.0, 0.0, 0.704]
    },
    {
        "name": "Georgia",
        "region": 1,
        "division": 4,
        "rank": 56,
        "points": [0.0, 0.0, 0.0, 0.620]
    },
    {
        "name": "Luxembourg",
        "region": 1,
        "division": 4,
        "rank": 57,
        "points": [0.0, 0.0, 0.0, 0.575]
    },
    {
        "name": "Israel",
        "region": 1,
        "division": 4,
        "rank": 58,
        "points": [0.0, 0.0, 0.0, 0.383]
    },
    {
        "name": "Afghanistan",
        "region": 3,
        "division": 3,
        "rank": 59,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Bolivia",
        "region": 2,
        "division": 2,
        "rank": 60,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Bosnia & Herzegovina",
        "region": 1,
        "division": 4,
        "rank": 61,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Dominican Republic",
        "region": 2,
        "division": 2,
        "rank": 62,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Iceland",
        "region": 1,
        "division": 4,
        "rank": 63,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Jamaica",
        "region": 2,
        "division": 2,
        "rank": 64,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Kosovo",
        "region": 1,
        "division": 4,
        "rank": 65,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Kuwait",
        "region": 3,
        "division": 3,
        "rank": 66,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Mongolia",
        "region": 3,
        "division": 3,
        "rank": 67,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Serbia",
        "region": 1,
        "division": 4,
        "rank": 68,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Thailand",
        "region": 3,
        "division": 3,
        "rank": 69,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Turkmenistan",
        "region": 3,
        "division": 3,
        "rank": 70,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "U.S. Virgin Islands",
        "region": 2,
        "division": 2,
        "rank": 71,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Puerto Rico",
        "region": 2,
        "division": 2,
        "rank": 72,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Pakistan",
        "region": 3,
        "division": 3,
        "rank": 73,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
    {
        "name": "Monaco",
        "region": 1,
        "division": 4,
        "rank": 74,
        "points": [0.0, 0.0, 0.0, 0.0]
    },
]