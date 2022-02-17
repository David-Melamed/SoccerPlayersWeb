import requests
import json

url = "http://localhost:8080/teams/"

new_team = {
        "city": "Manchester",
        "country": "England",
        "start_date": None,
        "League": "Premier League",
        "coach_name": "Pep Guardiola",
        "url": "https://www.seekpng.com/png/detail/15-159909_manchester-city-fc-badge-man-city-logo-png.png"
    }

payload = json.dumps(new_team)
headers = {
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
