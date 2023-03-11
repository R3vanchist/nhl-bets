import requests
import datetime
import json

def schedule():
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
        dailyGames = []
        # iterate over the games and print the information
        i = 0
        for game in games:
            away_team = game["teams"]["away"]["team"]["name"]
            #away_abbr = game["teams"]["away"]["team"]["abbreviation"]
            home_team = game["teams"]["home"]["team"]["name"]
            #home_abbr = game["teams"]["home"]["team"]["abbreviation"]
            i += 1
            dailyGames.append({
                'Game': i,
                'Away Team': away_team,
                'Home Team': home_team
            })
        filename = f'todays_games.json'
        with open(filename, 'w') as f:
            json.dump(dailyGames, f)
        
    else:
        print(f"Error retrieving NHL schedule: {response.status_code}")
