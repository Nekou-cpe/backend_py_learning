'''fibonatchi by generator'''
def fib_generator(n):
    a=0
    b=1
    yield a,b
    for i in range(1,n):
        a,b=b,a+b
        yield b

list1=[x for x in fib_generator(10)]
print(list1)