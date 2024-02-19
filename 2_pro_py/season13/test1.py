import requests
import re #this is too hard scraping data and search with re
res1=requests.get("https://translate.google.com/")#content is all website
print(res1.status_code)# status code: 200->complete
#print(res1.text)#access content of website
list_title=list(re.findall(r"<title>(.*)</title>",res1.text))#find pice of code with regex
print(list_title)
