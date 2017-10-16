import urllib.request
import bs4
from bs4 import BeautifulSoup

url = 'http://news.ncu.edu.cn/'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res.read(),'html.parser',from_encoding='utf-8')
node_title = soup.find('title')
title = node_title.get_text()
news = soup.select('.bknews')
print(title)
print('南大要闻：')
for new in news:
	print('-',new.get_text())
	
Creating a new branch is quick AND simple.