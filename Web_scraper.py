import requests
from bs4 import BeautifulSoup

# Specify the URL of the player's stats page
url = 'https://www.hockey-reference.com/players/m/meierti01/gamelog/2023'

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find the table containing the player's game stats
table = soup.find('table', {'id': 'gamelog'})

# Find all rows in the table
rows = table.find_all('td')

# Loop through the last 10 rows (excluding the header row)
for row in rows[1316:]:
    cells = str(row)
    if '"goals"' in cells:
        print(cells)
    # Extract the data from each cell in the row
"""     goals = rows[2].text.strip()
    assists = rows[3].text.strip()
    points = rows[4].text.strip()
    
    # Print the data
    print(f"G: {goals}, A: {assists}, P: {points}") """
