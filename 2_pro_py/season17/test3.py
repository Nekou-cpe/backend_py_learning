import requests
import json

parametr={'rel_rhy':'jingle'}
response=requests.get('http://api.datamuse.com/words',parametr)
if response.status_code==200:
    print(response.json())
    

else:
    print(f'error{response.status_code}')