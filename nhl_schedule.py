import requests
import datetime

def schedule():
    today = datetime.date.today()

    # format the date in the required format for the API (YYYY-MM-DD)
    date_str = today.strftime("%Y-%m-%d")

    # make the API request to retrieve the daily schedule
    url = f"https://statsapi.web.nhl.com/api/v1/schedule?date={date_str}&expand=schedule.teams"
    response = requests.get(url)

    filename = 'todays_games.txt'
    with open(filename, 'w') as todays_teams:
        # check if the request was successful
        if response.status_code == 200:
            # parse the JSON response
            data = response.json()
            
            # extract the game information from the response
            games = data["dates"][0]["games"]
            i = 1
            # iterate over the games and print the information
            for game in games:
                away_team = game["teams"]["away"]["team"]["name"]
                away_abbr = game["teams"]["away"]["team"]["abbreviation"]
                home_team = game["teams"]["home"]["team"]["name"]
                home_abbr = game["teams"]["home"]["team"]["abbreviation"]
                todays_teams.write(f"{i} {away_team}, {away_abbr} @ {home_team}, {home_abbr}\n")
                i = i + 1
        else:
            print(f"Error retrieving NHL schedule: {response.status_code}")
