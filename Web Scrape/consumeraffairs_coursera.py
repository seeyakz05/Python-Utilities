from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

BASE_URL = r'https://www.consumeraffairs.com/education/online-courses/coursera.html?page='
pages = [1, 2]

df = pd.DataFrame(columns=['Rating', 'Verified Buyer', 'Verified Reviewer', 'Reviewer Name',
							'Review Date', 'Review'])

for page in pages:
	req = requests.get(BASE_URL + str(page))
	soup = BeautifulSoup(req.content, 'html.parser')

	review_container = soup.find('div', attrs={'id':'reviews-container'})
	divs = review_container.find_all('div', attrs={'class':'rvw js-rvw', 'itemprop':re.compile(r'reviews')})

	for div in divs:

		# the review block consisted of 4 parts: header, author, body, footer
		header = div.find('div', attrs={'class':'rvw__hdr-stat'})
		rating = ''
		try:
			rating = header.find('div', attrs={'class':'stars-rtg stars-rtg--sm'})['data-rating'] 
		except Exception:
			try:
				rating = header.img['data-rating']
			except Exception:
				pass

		# directly call the tag then wrap with attribute value
		author = div.find('div', attrs={'class':'rvw-aut'})
		reviewer_name = author.find('strong', attrs={'itemprop':'author'}).text
		verified_buyer = ''
		verified_reviewer = ''
		for review in author.find_all('strong', attrs={'class':'rvw-aut__inf-ver'}):
			if review.text.strip().endswith('Buyer'):
				verified_buyer = review.text.strip()
			elif review.text.strip().endswith('Reviewer'):
				verified_reviewer = review.text.strip()

		body = div.find('div', attrs={'class':'rvw-bd ca-txt-bd-2'})
		review_date = body.span.text

		review_comment=''
		for p in body.find_all('p'):
			if not p.text in review_comment:
				review_comment += p.text + '\n' + ' \n'

		df = df.append({'Rating':rating, 'Verified Buyer':verified_buyer, 'Verified Reviewer':verified_reviewer, 'Reviewer Name':reviewer_name, 'Review Date':review_date, 'Review':review_comment}, ignore_index=True)
	
df.to_csv('test.csv', index=False)
