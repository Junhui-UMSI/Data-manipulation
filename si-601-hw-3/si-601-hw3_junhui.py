from bs4 import BeautifulSoup
import json, urllib2,re


####### Step 1
response = urllib2.urlopen('http://www.imdb.com/search/title?at=0&sort=num_votes&count=100')
initial_doc = response.read()
soup = BeautifulSoup(initial_doc,'html.parser')

outputfile = open ("step1.html",'w')
outputfile.write(soup.encode('utf-8'))
outputfile.close()

####### Step 2
inputfile = open('step1.html','rU')
outputfile = open('step2.txt','w')
soup = BeautifulSoup(inputfile,'html.parser')

outputfile.write("   ".join(['IMDB_ID','Rank','Title'])+'\n')

IMDBdiv = soup.find_all('h3',class_='lister-item-header')
IMDBlink = []
for item in IMDBdiv:
    link = item.find_all('a')
    for a in link:
        IMDBlink.append(a['href'])
print IMDBlink
for link in IMDBlink:
    match = re.match(r'',link)
