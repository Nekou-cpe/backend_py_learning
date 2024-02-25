import requests
import json

response=requests.get('http://api.datamuse.com/words?rel_rhy=jingle')
if response.status_code==200:
    jsonData=response.json()
    jsonStrData=json.dumps(jsonData,indent=2)
    print(jsonStrData)
    

else:
    print(f'error{response.status_code}')