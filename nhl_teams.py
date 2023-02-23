import csv
import json

def conv_csv_json():
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

    with open('nhl_data.json', 'w') as jsonfile:
        jsonfile.write(json_string)
conv_csv_json()

def compare_json_txt():
    with open('todays_games.txt', 'r') as games, open('nhl_data.json', 'r') as stats:
        txt_data = games.read()
        json_data = json.load(stats)
        # Compare the text data to the JSON data
        for team in json_data:
            goals_for = team['G/G']
            goals_against = team['GA/G']
            tEAM = team['TEAM']
            break_between = '='*30
            total = float(goals_for) + float(goals_against)
            if team['TEAM'] in txt_data:
                print(f"{break_between}\nTeam: {tEAM}\nGoals per game: {goals_for}\nGoals against per game: {goals_against}")
                print(f"Total: {total}")
compare_json_txt()
