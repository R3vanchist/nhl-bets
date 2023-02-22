import requests
import datetime

# set the date to today
today = datetime.date.today()

# format the date in the required format for the API (YYYY-MM-DD)
date_str = today.strftime("%Y-%m-%d")

# make the API request to retrieve the daily schedule
url = f"https://statsapi.web.nhl.com/api/v1/schedule?date={date_str}&expand=schedule.teams"
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
    # parse the JSON response
    data = response.json()
    
    # extract the game information from the response
    games = data["dates"][0]["games"]
    
    # iterate over the games and print the information
    for game in games:
        away_team = game["teams"]["away"]["team"]["name"]
        home_team = game["teams"]["home"]["team"]["name"]
        game_time = game["gameDate"]
        print(f"{away_team} @ {home_team} ({game_time})")
else:
    print(f"Error retrieving NHL schedule: {response.status_code}")
