'''local and global variables'''
#global variable
def func1():
    #creat global
    global c
    global k
    k=50
    #local variable
    x=5
    #this is just in function
    y=7
    print('inside func',x,y,c,k)
    #x=5 error
x=10
x=x*2
c=80
func1()
print('out of func',x,c,k)
