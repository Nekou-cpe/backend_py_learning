'''useful function6: dictionary function:
get key value item setdefault'''
dict1={
    'name':'Nekou',
    'last name':'Dfrm',
    'age':20,
    'from':'nowhere'
}
print(dict1.items())
print(dict1.values())
print(dict1.keys())
print(dict1.get('name'))#same as dict1['name']

str1='Nekou nila shakir sara sam nikol'
dict2={}
for char in str1:
    dict2.setdefault(char,0)
    dict2[char]+=1

print(dict2)