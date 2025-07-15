import requests
from bs4 import BeautifulSoup 
url='https://translate.google.com/?sl=en&tl=fa&op=translate'
res=requests.get(url)
print(res.status_code)
#beautifulsoup works with html so you should use res.text or res.content to access body
soup=BeautifulSoup(res.text,'html.parser')
list_img=soup.find_all('img')
list_img_url=[]
counter=0
for i in list_img:
    img_src=i['src']
    if not img_src.startswith('http'):
        img_url= url + img_src
    list_img_url.append(img_url)
    img_data=requests.get(img_url).content
    counter=+1
    with open(f'd:\\darsman\\codes\\backent_py_learning\\2_pro_py\\season13 downloaded_image{counter}.jpg', 'wb') as img_file:
        img_file.write(img_data)
        print("Image downloaded successfully!")
    