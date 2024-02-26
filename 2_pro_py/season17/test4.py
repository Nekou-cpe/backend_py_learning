import requests
import json
parameter={'q':'Berlin','appid':'d2fd3345bc920090a0b68d6826f9bbb4'}
response=requests.get('https://api.openweathermap.org/data/2.5/weather?',parameter)
if response.status_code==200:
    jsonData=response.json()
    mainInfo=jsonData['main']
    print(mainInfo['temp'])
else:
    print('error is : ',response.status_code)