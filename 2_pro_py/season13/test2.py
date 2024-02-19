import requests
from bs4 import BeautifulSoup

res1=requests.get("https://translate.google.com/")
soup=BeautifulSoup(res1.content,"html.parser")#what typ is your code inside website you chose?
print(soup.title)#shows title of website
print(soup.body)#shows body of html
print(soup.head)#shows head of html



