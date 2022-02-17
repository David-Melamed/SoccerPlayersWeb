import re

import requests
import json

url = "http://localhost:8080/players/"

new_player = {
  "first_name": "Raheem",
  "last_name": "Sterling",
  "start_date": "2015-07-14 00:00:00",
  "position": "Forward",
  "salary": "9500000",
  "team": "Manchester",
  "url": "https://www.footballdatabase.eu/images/photos/players/a_97/97498.jpg"
}

payload = json.dumps(new_player)
headers = {
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
