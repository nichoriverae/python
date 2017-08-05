#learning to webscrape in python

#import the library used to query a website
import urllib2
wiki = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_india'

#open the web page
page = urllib2.urlopen(wiki)

#import BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

