import requests

def get_data_leagus(link:str,league_id, date, season):
    
    __header={
       # "x-rapidapi-host":"v3.football.api-sports.io",
        #"x-rapidapi-key":"f7919498dc3463f309110e3c64e84ed8"
        "x-apisports-key":"f7919498dc3463f309110e3c64e84ed8"
        #"x-rapidapi-key":"f7919498dc3463f309110e3c64e84ed8"
    }
    
    params = {
        "league": league_id,
        "date": date,
        "season": season
    }

    response = requests.get(link, headers=__header, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        print(response.text)
        
        return data['response']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
 # ضع مفتاح API الخاص بك هنا
league_id = 39           # مثال: الدوري الإنجليزي الممتاز
date = "2020-12-1"      # حدد التاريخ المطلوب
season = 2021     
# الموسم المطلوب
link="https://v3.football.api-sports.io/fixtures"
matches = get_data_leagus(link,league_id, date, season)

    
#get_data_leagus("https://v3.football.api-sports.io/leagues/")

    
   
   
   
   
   
    
data = {
    "get": "leagues",
    "parameters": [],
    "errors": [],
    "results": 1169,
    "paging": {
        "current": 1,
        "total": 1
    },
    "response": [
        {
            "league": {
                "id": 4,
                "name": "Euro Championship",
                "type": "Cup",
                "logo": "https://media.api-sports.io/football/leagues/4.png"
            },
            "country": {
                "name": "World",
                "code": None,
                "flag": None
            },
            "seasons": [
                {
                    "year": 2008,
                    "start": "2008-06-07",
                    "end": "2008-06-29",
                    "current": False,
                    "coverage": {
                        "fixtures": {
                            "events": True,
                            "lineups": True,
                            "statistics_fixtures": False,
                            "statistics_players": False
                        },
                        "standings": False,
                        "players": True,
                        "top_scorers": True,
                        "top_assists": True,
                        "top_cards": True,
                        "injuries": False,
                        "predictions": True,
                        "odds": False
                    }
                },
                {
                    "year": 2012,
                    "start": "2012-06-08",
                    "end": "2012-07-01",
                    "current": False,
                    "coverage": {
                        "fixtures": {
                            "events": True,
                            "lineups": True,
                            "statistics_fixtures": False,
                            "statistics_players": False
                        },
                        "standings": False,
                        "players": True,
                        "top_scorers": True,
                        "top_assists": True,
                        "top_cards": True,
                        "injuries": False,
                        "predictions": True,
                        "odds": False
                    }
                }
            ]
        },
        {
            "league": {
                "id": 21,
                "name": "Confederations Cup",
                "type": "Cup",
                "logo": "https://media.api-sports.io/football/leagues/21.png"
            },
            "country": {
                "name": "World",
                "code": None,
                "flag": None
            },
            "seasons": [
                {
                    "year": 2009,
                    "start": "2009-06-14",
                    "end": "2009-06-28",
                    "current": False,
                    "coverage": {
                        "fixtures": {
                            "events": True,
                            "lineups": True,
                            "statistics_fixtures": False,
                            "statistics_players": False
                        },
                        "standings": False,
                        "players": True,
                        "top_scorers": True,
                        "top_assists": True,
                        "top_cards": True,
                        "injuries": False,
                        "predictions": True,
                        "odds": False
                    }
                }
            ]
        }
    ]
}



