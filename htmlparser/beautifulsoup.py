import urllib.request
from bs4 import BeautifulSoup

bs = urllib.request.urlopen("http://www.domainname")
#print(bs.code)
bt = BeautifulSoup(bs.read(), 'lxml')

#title of webpage
# print(bt.title.string)

#get all metatags
#print(bt.find_all('meta'))


# allMetaTags = bt.find_all('meta')
# print(allMetaTags[2]['content'])
# print(allMetaTags[2]['name'])

#extracting all urls
# for link in bt.find_all('a'):
# 	print(link.get('href'))

#extracting all the text
print(bt.get_text())
