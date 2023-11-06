'''tuple'''

#list to tuple and tuple to list
tuple1=('Neko','Dfrm',20)
tempList=list(tuple1)
tempList.append('cp')
tuple1=tempList
print(tuple1)

#nested list and tuple
tuple2=([2,5,5,6,7],[5,6,734,42,45],[4,97,34,23],(3,43,3434,3432))
list1=[['fkls','sj','sd',(12,21,32,222),'kxj'],['djs','sdk',98],(1,211,908)]
print(tuple2[1][2])
print(list1[0][3][1])
