import requests
from bs4 import BeautifulSoup
res=requests.get('https://webscraper.io/')
soup=BeautifulSoup(res.content,'html.parser')
items=soup.select('body')
for item in items:
    print(item.select('div.container'))

