import requests
import json

def team_stat_pull():
    season = '20222023'
    endpoint = f'https://statsapi.web.nhl.com/api/v1/teams?expand=team.stats&season={season}'
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        teams = data['teams']
        stats = []
        for team in teams:
            team_stats = team['teamStats'][0]['splits'][0]['stat'] # change the index to get different stats
            team_name = team['name']
            points_per_game = team_stats['goalsPerGame']
            points_against_per_game = team_stats['goalsAgainstPerGame']
            total = points_per_game + points_against_per_game
            stats.append({
                'Team': team_name,
                'Points per Game': points_per_game,
                'Points Against per Game': points_against_per_game,
                'Total': total
            })
        
        filename = f'nhl_team_stats_{season}.json'
        with open(filename, 'w') as f:
            json.dump(stats, f)
