import requests
import datetime
import pandas as pd
import nhl_schedule
import nhl_teams

def nhl_player_stats():
    # Enter the player's name and team
    player_name = input("Enter player's name: ")
    team_name = input("Enter team name: ")

    # Create the URL to get the team's id
    team_url = f"https://statsapi.web.nhl.com/api/v1/teams/"
    team_response = requests.get(team_url)
    team_data = team_response.json()
    team_id = None
    for team in team_data["teams"]:
        team_names = team["name"]
        team_ids = team["id"]
        if team_name in team_names:
            team_id = team_ids

    # Create the URL to get the player's id

    player_url = f"https://statsapi.web.nhl.com/api/v1/teams/{team_id}/roster"
    player_response = requests.get(player_url)
    player_data = player_response.json()
    player_id = None
    for players in player_data["roster"]:
        playerName = players["person"]["fullName"]
        playerId = players["person"]["id"]
        if player_name in playerName:
            player_id = playerId

    # Create the URL to get the player's game log
    stats_url = f"https://statsapi.web.nhl.com/api/v1/people/{player_id}/stats?stats=gameLog&season=20222023"
    stats_response = requests.get(stats_url)
    stats_data = stats_response.json()

    # Create a pandas dataframe with the player's last 10 games' stats
    stats = stats_data['stats'][0]['splits'][:10
    ]
    player_stats = []
    for game in stats:
        game_stats = {
            'Shots': game['stat']['shots'],
            'Goals': game['stat']['goals'],
            'Assists': game['stat']['assists'],
            'Points': game['stat']['points'],
            }
        player_stats.append(game_stats)

    df = pd.DataFrame(player_stats)
    print(df)



nhl_schedule()
nhl_teams()
nhl_player_stats()
