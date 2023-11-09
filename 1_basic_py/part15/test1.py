'''list'''

#str to list + list to str
name='Nekou'
temp=list(name)
temp[1]='E'
name = ''.join(temp)
print(name)

#list things
list1=[1,2,3,4,5,6]
list1.append(7)
print(list1)
list1.extend([8,9,10])
print(list1)
list1.remove(4)
print(list1)
list2=[11,11,22,33,'hello',44,'bye']
for th in list2:
    if type(th)==str:    
        print(th)
print(list1.count(22))