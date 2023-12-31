'''Decorators 2'''
def mainFunction1(func):
    def function1(*args,**kwargs):
        x=func(*args,**kwargs)
        return x+x
    return function1

def mainFunction2(func):
    def function2(*args,**kwargs):
        x=func(*args,**kwargs)
        return x**x
    return function2

def mainFunction3(func):
    def function3(*args,**kwargs):
        x=func(*args,**kwargs)
        return x*x
    return function3

@mainFunction1
@mainFunction2
@mainFunction3
def func1():
    return 20

@mainFunction1
def summ(z,y):
    return z+y
print(func1)
print(summ)