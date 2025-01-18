import requests
import json
def get_team_transfers(team_id):
    url = "https://v3.football.api-sports.io/transfers"
    headers = {
        "x-apisports-key": "2be8169e016e5c7cc5379ec0405defb6"
    }
    params = {
        "team": team_id
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "response" in data and data['response']:
        return data['response']
    else:
        print("No transfer data found or an error occurred.")
        return []

# استبدل "YOUR_API_KEY" بمفتاح API الخاص بك، و"40" بمعرف الفريق الذي ترغب في جلب انتقالاته
transfers = get_team_transfers(team_id=40)
print(json.dumps(transfers[2],indent=4))

# for transfer in transfers:
#     player_info = transfer['player']
#     transfer_info = transfer['transfers'][0]
#     print(f"Player: {player_info['name']}")
#     print(f"From: {transfer_info['teams']['out']['name']}")
#     print(f"To: {transfer_info['teams']['in']['name']}")
#     print(f"Date: {transfer_info['date']}")
#     print(f"Type: {transfer_info['type']}")
#     print("------")