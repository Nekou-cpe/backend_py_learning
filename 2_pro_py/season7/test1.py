'''Decoratior definition basic'''
#point one: functon is an object so you can creat new object by this function
def function1(name):
    return f'Hello {name}'

print(function1('Sara'))
function2=function1
print(function2('Nekou'))
del function1
print(function2('Nekolj'))
#print(function1('Sara')) -> this an Error
print('################################')
#point two: nested function ->the function inside other function just callable inside that function
def function3(fname):
    print('this is inside func3'+fname)
    lname=input('last name: ')
    def function4(lname):
        return f'this is inside func4 lname is {lname}'
    print('this is inside func3'+fname)
    print(function4(lname))

function3('Aria')
print('################################')
#point three: input a func can be another func
def function5(something):
    return f'***{something}***'

def function6(smth):
    listt=[]
    for i in range(3):
        listt.append(smth)
    return listt

def mainFunction(func):
    inside=input('enter something')
    return func(inside)

print(mainFunction(function6))
print(mainFunction(function5))
print('################################')
#point four: output of function will other function
def calculator(n):
    def sum(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def div(x,y):
        return x//y
    def mul(x,y):
        return x*y
    def pow(x,y):
        return x**y
    if n==1:
        return sum
    elif n==2:
        return sub
    elif n==3:
        return div
    elif n==4:
        return mul
    elif n==5:
        return pow

for j in range(1,6):
    k=calculator(j)
    print(k(30,3))
    
