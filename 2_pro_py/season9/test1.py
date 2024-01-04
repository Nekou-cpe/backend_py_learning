'''packing , unpacking'''
#packing:
list1=[1,23,4,5,24,76]
print(*list1)
print('----------------')
dict1={'a':1,'b':2,'c':3}
print(*dict1)
print('----------------')
def func2(a,b,c,d):
    print(a,b,c,d)
list2=[9,8,7,6]
func2(*list2)
print('----------------')
def func3(*args):
    for item in args:
        print(item)
        
func3(23,4,5,67,7)
print('----------------')
#dictionary packing
def func4(**kwargs):
    for key in kwargs:
        print(key,kwargs[key])

dict2={'a':9,'b':8,'c':2}
func4(**dict2)
print('----------------')
#unpacking
def func8(h,m,s):
    print(h,m,s)
    
list4=[56,5,6]
func8(*list4)
print('----------------')
#packing and unpacking 
def func6(k,l,n,t):
    print(k,l,n,t)
    
def func5(*args):
    list6=list(args)
    list6.append('sara')
    list6[2]='Nekou'
    func6(*list6)
list5=['Nikolj','Yuri','Sam']   
func5(*list5)
print('----------------')