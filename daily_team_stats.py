import json


def team_scoring_three():
    with open('nhl_team_stats_20222023.json','r') as file, open('todays_games.json','r') as file2, open('bets.txt','w') as bets: 
        games = json.load(file2)
        statistics = json.load(file)
        bets.write(f'Teams likely to score over 3 goals: \n')

        for game in games:
            for team in statistics:
                if game['Away Team'] == team['Team']:
                    game['Away Points per Game'] = team['Points per Game']
                    game['Away Points Against per Game'] = team['Points Against per Game']
                    game['Away Total'] = team['Total']
                elif game['Home Team'] == team['Team']:
                    game['Home Points per Game'] = team['Points per Game']
                    game['Home Points Against per Game'] = team['Points Against per Game']
                    game['Home Total'] = team['Total']

        for i in range(len(games)):
            homeTeam = games[i]['Home Team']
            homePoints = games[i]['Home Points per Game']
            homeAllowed = games[i]['Home Points Against per Game']
            homeTotal = games[i]['Home Total']
            awayTeam = games[i]['Away Team']
            awayPoints = games[i]['Away Points per Game']
            awayAllowed = games[i]['Away Points Against per Game']
            awayTotal = games[i]['Away Total']
            if homePoints > 3.0 and awayAllowed > 3.0:
                bets.write(f'{homeTeam}\n')
            if awayPoints > 3.0 and homeAllowed > 3.0:
                bets.write(f'{awayTeam}\n')
                
        sep = '=' *60
        bets.write(sep)


def team_not_scoring_three():
    with open('nhl_team_stats_20222023.json','r') as file, open('todays_games.json','r') as file2, open('bets.txt','a') as bets: 
        games = json.load(file2)
        statistics = json.load(file)
        bets.write(f'\nTeams not likely to score over 3 goals: \n')

        for game in games:
            for team in statistics:
                if game['Away Team'] == team['Team']:
                    game['Away Points per Game'] = team['Points per Game']
                    game['Away Points Against per Game'] = team['Points Against per Game']
                    game['Away Total'] = team['Total']
                elif game['Home Team'] == team['Team']:
                    game['Home Points per Game'] = team['Points per Game']
                    game['Home Points Against per Game'] = team['Points Against per Game']
                    game['Home Total'] = team['Total']

        for i in range(len(games)):
            homeTeam = games[i]['Home Team']
            homePoints = games[i]['Home Points per Game']
            homeAllowed = games[i]['Home Points Against per Game']
            homeTotal = games[i]['Home Total']
            awayTeam = games[i]['Away Team']
            awayPoints = games[i]['Away Points per Game']
            awayAllowed = games[i]['Away Points Against per Game']
            awayTotal = games[i]['Away Total']
            if homePoints < 3.0 and awayAllowed < 3.0:
                bets.write(f'{homeTeam}\n')
            if awayPoints < 3.0 and homeAllowed < 3.0:
                bets.write(f'{awayTeam}\n')
        sep = '=' *60
        bets.write(sep)

def team_overs():
    with open('nhl_team_stats_20222023.json','r') as file, open('todays_games.json','r') as file2, open('bets.txt','a') as bets: 
        games = json.load(file2)
        statistics = json.load(file)
        bets.write(f'\nGames likely to go over 6 goals: \n')

        for game in games:
            for team in statistics:
                if game['Away Team'] == team['Team']:
                    game['Away Points per Game'] = team['Points per Game']
                    game['Away Points Against per Game'] = team['Points Against per Game']
                    game['Away Total'] = team['Total']
                elif game['Home Team'] == team['Team']:
                    game['Home Points per Game'] = team['Points per Game']
                    game['Home Points Against per Game'] = team['Points Against per Game']
                    game['Home Total'] = team['Total']

        for i in range(len(games)):
            homeTeam = games[i]['Home Team']
            homePoints = games[i]['Home Points per Game']
            homeAllowed = games[i]['Home Points Against per Game']
            homeTotal = games[i]['Home Total']
            awayTeam = games[i]['Away Team']
            awayPoints = games[i]['Away Points per Game']
            awayAllowed = games[i]['Away Points Against per Game']
            awayTotal = games[i]['Away Total']
            if homePoints > 3.0 and awayAllowed > 3.0 and awayPoints > 3.0:
                bets.write(f'{awayTeam} @ {homeTeam}\n')
            if awayPoints > 3.0 and homeAllowed > 3.0 and homePoints > 3.0:
                bets.write(f'{awayTeam} @ {homeTeam}\n')

        sep = '=' *60
        bets.write(sep)

def team_unders():
    with open('nhl_team_stats_20222023.json','r') as file, open('todays_games.json','r') as file2, open('bets.txt','a') as bets: 
        games = json.load(file2)
        statistics = json.load(file)
        bets.write(f'\nGames likely to go under 6 goals: \n')

        for game in games:
            for team in statistics:
                if game['Away Team'] == team['Team']:
                    game['Away Points per Game'] = team['Points per Game']
                    game['Away Points Against per Game'] = team['Points Against per Game']
                    game['Away Total'] = team['Total']
                elif game['Home Team'] == team['Team']:
                    game['Home Points per Game'] = team['Points per Game']
                    game['Home Points Against per Game'] = team['Points Against per Game']
                    game['Home Total'] = team['Total']

        for i in range(len(games)):
            homeTeam = games[i]['Home Team']
            homePoints = games[i]['Home Points per Game']
            homeAllowed = games[i]['Home Points Against per Game']
            homeTotal = games[i]['Home Total']
            awayTeam = games[i]['Away Team']
            awayPoints = games[i]['Away Points per Game']
            awayAllowed = games[i]['Away Points Against per Game']
            awayTotal = games[i]['Away Total']
            if homePoints < 3.0 and awayAllowed < 3.0 and awayPoints < 3.0:
                bets.write(f'{awayTeam} @ {homeTeam}\n')
            if awayPoints < 3.0 and homeAllowed < 3.0 and homePoints < 3.0:
                bets.write(f'{awayTeam} @ {homeTeam}\n')

        sep = '=' *60
        bets.write(sep)
        bets.write(f"\nGood luck tonight and don't forget to check those goalies!")
