import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

columns = ['Season', 'Player Name', 'Conference', 'Date',
           'Team', 'Pos', 'Height', 'Weight',
           'Age', 'PreDraftTeam', 'DraftYear', 'YOS']
df = pd.DataFrame(columns=columns)

table = soup.find('table', {'class':'tablesaw', 'data-tablesaw-mode':'swipe'}).tbody
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n','') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)
    
df.to_csv('nba player of the week.csv', index=False)    
