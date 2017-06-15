#Generate Movie Quote

from bs4 import BeautifulSoup
from lxml import html
import requests
import random

def generateMovieQuote():
	quote="null"
	movie="null"

	while quote=="null" or movie=="null":
		#url = "http://www.moviequotes.com/archive/bynumber/"+str(random.randint(100,5000))+".html"
		url="http://www.moviequotes.com/archive/bynumber/2336.html"
		print "requesting url: ",url

		page = requests.get(url,timeout=5)
		htmltxt = page.text

		soup = BeautifulSoup(htmltxt,'lxml')
		data = soup.text.split("\n")
		for temp in data:
			if "Quote:" in temp:
				quote = temp[7:]
			elif "Movie Title:" in temp:
				movie = temp[13:]

	text = "\""+quote+"\"\n from "+movie			
	print text

	return text


#generateMovieQuote()