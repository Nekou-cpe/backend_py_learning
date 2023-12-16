'''useful function5: set function:
difference union intersection issubset'''
set1={1,2,3,4,5,6,7,12,14,16,21,54}
set2={78,45,52,54,3,27,15,51,511,55,78}
set12={1,2,3}
set3=set1.difference(set2)#set1-set2
set4=set2.difference(set1)#set2-set1
set5=set1.union(set2)#set1 or set2
set6=set1.intersection(set2)#set1 and set2
set7=set1.issubset(set2)#set1 is sub set set2
set8=set12.issubset(set1)
print(set3)
print(set4)
print(set5)
print(set6)
print(set7)
print(set8)

