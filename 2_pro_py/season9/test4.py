'''send generator'''
from random import randint
def generator1():
    x=10
    yield x
    yield x+10
    yield x*2

def generator2():
    x=10
    x=yield x
    x=yield x+10
    yield x*2

def generator3():
    while True:
        x=yield 500
        x=yield x+10
        yield x*2
        
def generator4(func):
    while True:
        x=randint(1,100)
        func.send(x)
        yield
def generator5():
    while True:
        x=yield
        print(x,end=' ')
        

g1=generator1()
print(next(g1))
print(next(g1))
print(next(g1))
print()
g2=generator2()
print(next(g2))
print(g2.send(2))
print(g2.send(3))
print()
g3=generator3()
print(next(g3))
print(g3.send(20))
print(g3.send(3))
print(g3.send(3))#first always should be next 0r none send
print()
g5=generator5()
g5.send(None)#working same next
g4=generator4(g5)
for i in range(10):
    next(g4)



