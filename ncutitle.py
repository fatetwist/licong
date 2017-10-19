import urllib.request
import bs4
from bs4 import BeautifulSoup

# Web
url='http://news.ncu.edu.cn/'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res.read(),'html.parser',from_encoding='utf-8')
# 网页标题
node_title = soup.find('title')
title = node_title.get_text()
# 其他标题
title_others = soup.findAll('ul',{'class':{'newslist'}})
print(title)
for y in title_others:
    print(y.get_text())
