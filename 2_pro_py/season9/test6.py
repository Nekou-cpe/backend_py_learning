'''map filter reduce'''
from functools import reduce
#map: structure: list(map(func,value)) value can be any iterable structure
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=[11,12,13,14,15,343,435,6543]
list4=list(map(lambda *args: sum(args)/len(args),list1,list2,list3))
print(list4)
def func1(*args):
    listt=[]
    for i in range(len(args)):
        x=args[i]**args[i]
        listt.append(x)
    return listt
list5=list(map(func1,[10,9,3]))
print(list5)   
#filter:structure:list(filter(func,value)) return value when works func right (TRUE)
list6=list(filter(lambda x:str(x).find('43')!=-1,list3 ))
print(list6)
#reduce -> same as filter and map but return just result
reduce1=reduce(lambda x,y: x+y,list3)
print(reduce1)