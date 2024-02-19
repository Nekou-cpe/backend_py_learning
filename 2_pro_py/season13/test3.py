import requests
from bs4 import BeautifulSoup
import os
print(os.path.realpath)
with open('html\\youtube.html') as youtube:
    soup=BeautifulSoup(youtube,'html.parser')
    print(soup.title)
    print(soup.find_all('img'))#listing all tags we want
    print(soup.find('a'))#finding first tag we want
    print(soup.select('.search'))#css seletor
    