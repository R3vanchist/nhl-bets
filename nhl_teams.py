import csv
import json
import requests
import datetime

def nhl_schedule():
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
            
            # iterate over the games and print the information
            for game in games:
                away_team = game["teams"]["away"]["team"]["name"]
                home_team = game["teams"]["home"]["team"]["name"]
                todays_teams.write(f"{away_team} @ {home_team}\n")
        else:
            print(f"Error retrieving NHL schedule: {response.status_code}")

nhl_schedule()

def conv_csv_json():
    with open('nhl_teams_season.csv', 'r') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)
        
        # Get the header row from the CSV file
        headers = next(csvreader)
        
        # Create an empty list to hold the rows of data
        data = []
        
        # Iterate over the remaining rows in the CSV file
        for row in csvreader:
            # Create a dictionary to hold the data for this row
            row_data = {}
            
            # Iterate over the columns in the row, and add them to the dictionary
            for i in range(len(headers)):
                row_data[headers[i]] = row[i]
            
            # Add the dictionary to the list of data
            data.append(row_data)

    # Convert the list of dictionaries to a JSON string
    json_string = json.dumps(data, indent=4)

    with open('nhl_data_season.json', 'w') as jsonfile:
        jsonfile.write(json_string)
conv_csv_json()

def compare_json_txt():
    with open('todays_games.txt', 'r') as games, open('nhl_data_season.json', 'r') as stats:
        txt_data = games.read()
        json_data = json.load(stats)
        # Compare the text data to the JSON data
        for team in json_data:
            goals_for = team['G/G']
            goals_against = team['GA/G']
            tEAM = team['TEAM']
            break_between = '='*30
            total = team['Total']
            #if team['TEAM'] in txt_data:
                #print(f"{break_between}\nTeam: {tEAM}\nGoals per game: {goals_for}\nGoals against per game: {goals_against}")
                #print(f"Total: {total}")
compare_json_txt()

def conv_csv_json_10():
    with open('nhl_data.csv', 'r') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)
        
        # Get the header row from the CSV file
        headers = next(csvreader)
        
        # Create an empty list to hold the rows of data
        data = []
        
        # Iterate over the remaining rows in the CSV file
        for row in csvreader:
            # Create a dictionary to hold the data for this row
            row_data = {}
            
            # Iterate over the columns in the row, and add them to the dictionary
            for i in range(len(headers)):
                row_data[headers[i]] = row[i]
            
            # Add the dictionary to the list of data
            data.append(row_data)

    # Convert the list of dictionaries to a JSON string
    json_string = json.dumps(data, indent=4)

    with open('nhl_data_10.json', 'w') as jsonfile:
        jsonfile.write(json_string)
conv_csv_json_10()

def compare_json_txt_10():
    with open('todays_games.txt', 'r') as games, open('nhl_data_10.json', 'r') as stats:
        txt_data = games.read()
        json_data = json.load(stats)
        # Compare the text data to the JSON data
        for team in json_data:
            goals_for = team['G/G']
            goals_against = team['GA/G']
            tEAM = team['TEAM']
            break_between = '='*30
            total = team['Total']
            #if team['TEAM'] in txt_data:
                #print(f"{break_between}\nTeam: {tEAM}\nGoals per game: {goals_for}\nGoals against per game: {goals_against}")
                #print(f"Total: {total}")
compare_json_txt_10()

def over_six_goals():
    # Load data from first file
    with open('nhl_data_10.json', 'r') as f:
        data1 = json.load(f)
    # Load data from second file
    with open('nhl_data_season.json', 'r') as f:
        data2 = json.load(f)
    with open('todays_games.txt', 'r') as file:
        games = file.read()
    # Compare data
    for team1, team2 in zip(data1, data2):
        if float(team1['Total']) > 6 and float(team2['Total']) > 6 and team1['TEAM'] in games:
            print(f"{team1['TEAM']} has a total score of {team1['Total']} in the last games 10 and {team2['Total']} for the season.")
over_six_goals()

print('='*90)

def under_six_goals():
    # Load data from first file
    with open('nhl_data_10.json', 'r') as f:
        data1 = json.load(f)
    # Load data from second file
    with open('nhl_data_season.json', 'r') as f:
        data2 = json.load(f)
    with open('todays_games.txt', 'r') as file:
        games = file.read()
    # Compare data
    for team1, team2 in zip(data1, data2):
        if float(team1['Total']) < 6 and float(team2['Total']) < 6 and team1['TEAM'] in games:
            print(f"{team1['TEAM']} has a total score of {team1['Total']} in the last games 10 and {team2['Total']} for the season.")
under_six_goals()
