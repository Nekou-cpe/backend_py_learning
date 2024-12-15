import demjson3 as demj
import os
import json
class Person():
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
        

    def __str__(self) -> str:
        return f'{self.fname},{self.lname}'

        
Person1=Person('Nekou','Dfrm')
Person2=Person('Nikol','Mrfd')
Person3=Person('Homa','hdr')
if not(os.path.exists('test2.json')):
    with open('test2.json','w+') as f1:
        f1.write(demj.encode(Person1.__dict__))
        f1.write(demj.encode(Person2.__dict__))
        f1.write(demj.encode(Person3.__dict__))
with open('test2.json','r') as f2:
    strr=f2.read()
    
data=demj.decode(strr)
for person in data:
    print(person)