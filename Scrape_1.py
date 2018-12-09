import bs4 as bs
from urllib.request import Request,urlopen
import requests
import csv
########halleluhaaaaaa###############
text_file = open("scrape.txt","w")
print()
########halleluhaaaaaa###############
print()
source4= Request("https://stackoverflow.com/tags", headers={'User-Agent':'Mozilla/5.0'})	#For sites with https
webpage=urlopen(source4).read()
soup4 = bs.BeautifulSoup(webpage,'lxml')
########halleluhaaaaaa###############
nav = soup4.nav
for div in soup4.find_all('a',class_='post-tag'):	#data you want to get. using F12 find the data you want to fetch
	text_file.write(div.text)	#Written in a file
	print(div.text)
