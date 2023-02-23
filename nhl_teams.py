import pandas as pd

# read in the data
data = pd.read_csv('nhl_data.csv')

# calculate the average goals scored by each team over the last 10 games
avg_goals = data.groupby('TEAM')['G'].mean()
avg_goals_against = data.groupby('TEAM')['GA'].mean()

# print the results
print(f"Average goals are: {avg_goals}")
print(f"Average goals against are: {avg_goals_against}")
