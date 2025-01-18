from page_filter_data_apifootball.leagues.utils import Top_goall_and_assist
import json


op=Top_goall_and_assist()
x=op.comparsone(
    "https://v3.football.api-sports.io/players/topscorers",

    "https://v3.football.api-sports.io/players/topassists",
    
    {
     "x-apisports-key": "2be8169e016e5c7cc5379ec0405defb6",

    },
    {
          
     "league": "39",  
     "season": "2024"

    }
)

print(json.dumps(x,indent=4))






