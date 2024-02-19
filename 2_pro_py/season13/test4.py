import requests
from bs4 import BeautifulSoup
res=requests.get('https://google.com')
soup=BeautifulSoup(res.content,'html.parser')
items=soup.body()
for item in items:
    print(item.select('div > a'))

