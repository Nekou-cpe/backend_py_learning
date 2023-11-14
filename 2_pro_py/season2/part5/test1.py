'''polymorphism
1)overloadin'''
from multipledispatch import dispatch 

@dispatch(int,int)
def summ(x,y):
    return x+y

@dispatch(int,int,int)
def summ(x,y,z):
    return x+y+z

print(summ(10,11))
print(summ(12,543,3))


