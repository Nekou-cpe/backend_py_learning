'''working with api'''
from PyPackage import requests
response=requests.get('http://api.datamuse.com/words?rel_rhy=jingle')
if response.status_code==200:
    print(response.status_code) #200 is status ok

    jsonData=response.json()
    print(jsonData[1]['word'])
    for data in jsonData:
        print(data)
else:
    print(f'error{response.status_code}')
    
