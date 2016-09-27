from bs4 import BeautifulSoup
import json, urllib2

response = urllib2.urlopen('http://www.imdb.com/search/title?at=0&sort=num_votes&count=100')
initial_doc = response.read()
soup = BeautifulSoup(initial_doc,'html.parser')

print soup