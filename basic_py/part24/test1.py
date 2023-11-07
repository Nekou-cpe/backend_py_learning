'''useful function3:list functin:
sort sorted reverse count copy pop'''

list1=[10,9,54,76,34,99,88,77,45,3,2,4,5,75,9,9,80]

#sort and sorted are sorting list but sort chang original list
print(sorted(list1))
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.count(9))
list1.pop()
print(list1)

#copy
list2=list1.copy()
list3=list1
list3.append(11)
print(list1)
print(list2)
print(list3)