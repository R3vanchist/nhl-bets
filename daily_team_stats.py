import json


def daily_stats():
    with open('todays_games.txt', 'r') as text, open('nhl_team_stats_20222023.json','r') as file: 
        games = text.read()
        statistics = json.load(file)
        for team in statistics:
            team_name = team['Team']
            goals_per_game = team['Points per Game']
            goals_against_per_game = team['Points Against per Game']
            total = team['Total']
            if team_name in games:
                print(f'{team_name}: {goals_per_game}, {goals_against_per_game}, and {total}')
