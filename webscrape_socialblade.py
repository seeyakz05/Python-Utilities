from bs4 import BeautifulSoup
from pandas import DataFrame
import requests
import re

URL = 'https://socialblade.com/youtube/top/trending/top-500-channels-30-days/most-subscribed'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')

body = soup.find('div', attrs={'style':'float: right; width: 900px;'})

table = body.find_all('div', style=re.compile(r'width: 860.*?'))

#skip the first two lines 
table = table[2:]

columns = ['Rank', 'Grade', 'Username', 'Uploads', 'Subs', 'VideoViews']

df = DataFrame(index = range(0, len(table)), columns=columns)

row = 0
for line in table:
	try:
		df.iloc[row, 0] = line.find('div', attrs={'style': 'float: left; width: 50px; color:#888;'}).text #Rank
	except:
		pass

	try:
		df.iloc[row, 1] = line.find(style=re.compile(r'font-weight:.*?')).text #Grade
	except:
		pass

	try:
		df.iloc[row, 2] = line.find('a').text #Username
	except:
		pass

	try:
		df.iloc[row, 3] = line.find(style=re.compile(r'color:#555.*?')).text #Uploads
	except:
		pass

	try:
		df.iloc[row, 4] = line.find_all('span')[2].text #Subs
	except:
		pass

	try:
		df.iloc[row, 5] = line.find_all('span')[3].text #VideoViews
	except:
		pass

	row +=1

df.to_csv(r'C:\Users\jjenn\Desktop\Test' + '\\top500.csv', index=False)
