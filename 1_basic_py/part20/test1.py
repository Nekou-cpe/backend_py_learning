import random
'''function2'''

#value in function
def fun1(name,familyname,age='none',number=None):
    print(f'my name is: {name}')
    print(f'my name is: {familyname}')    
    print(f'i am : {age} years old')
    if number is not None :
        print(f'number is :{number}')

#list in functions
def fun2(list1):
    for item in list1:
        print(item,end=' ')
    print('\n')


#function to list
def fun3(n):
    newlist=[]
    for i in range(n):
        newlist.append(random.randint(1,1000))
    return newlist


#any item add to function
def fun4(*arg):
    newSet=set()
    for item in arg:
        newSet.add(item)
    return newSet

loopNum=int(input('enter number of random: '))
fun1('Nekou','Dfrm','20',9348)
fun2([10,20,30,40,50])
print(fun3(loopNum))
print(fun4('hello','this is me',24,34,24))