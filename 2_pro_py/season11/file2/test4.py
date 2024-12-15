import json
person1={
    'name':'Niko',
    'lname':'Dadfarma',
    'age':21,
    'code':1278
}
person2={
    'name':'Niko',
    'lname':'Dadfarma',
    'age':21,
    'code':1278
}
person3={
    'name':'Niko',
    'lname':'Dadfarma',
    'age':21,
    'code':1278
}
persons=[person1,person2,person3]
with open('file1.json','a+') as f1:
    json.dump(persons,f1,indent=3)