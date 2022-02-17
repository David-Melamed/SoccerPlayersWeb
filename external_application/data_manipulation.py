from turtle import pd

import requests
import json
from datetime import datetime, timezone

url = "http://localhost:8080/my_app/"
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text.encode('utf8'))
final_dict = {}
final_dict['soccer_players'] = data

print(data)

with open("api_results.json", "w") as file:
    json.dump(final_dict, file, indent=2)

count_num_of_players_in_team = {}
count_salary_of_all_players = {}
players_start_date = {}
players_info = []

for player in data:
    player_full_name = player['first_name'] + ' ' + player['last_name']
    if player['team'] in count_salary_of_all_players.keys():
        count_salary_of_all_players.update(
            {player['team']: int(count_salary_of_all_players.get(player['team'])) + int(player['salary'])})
        count_num_of_players_in_team.update({player['team']: count_num_of_players_in_team.get(player['team']) + 1})
    else:
        count_salary_of_all_players.update({player['team']: 0})
        count_num_of_players_in_team.update({player['team']: 1})

    players_info.append([player['first_name'], player['last_name'], player['start_date'],
                         player['position'], player['salary'], player['team']])
    # player_start_date = player['start_date']
    # players_start_date.update({player_full_name : player_start_date})

salary_avg = {x: float(count_salary_of_all_players[x]) / count_num_of_players_in_team[x] for x in
              count_num_of_players_in_team}

with open("external_app_results.txt", "w") as file:
    for player_info in players_info:
        if float(player_info[4]) < salary_avg.get(player_info[5]):
            player_start_date = datetime.strptime(player_info[2], "%Y-%m-%dT%H:%M:%S")
            if (datetime.now() - player_start_date).total_seconds() < 31556926:
                for x in range(0, len(player_info)):
                    file.write(player_info[x] + "\n")
                file.write("\n")
print("Completed!")
##filter(lambda person: person['name'] == 'Pam', people)

# def search(firstname, lastname):
#     for p in data:
#         if p['first_name'] == firstname and p['last_name'] == lastname:
#             return p
