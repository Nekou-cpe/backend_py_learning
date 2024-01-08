'''timeit: calculate time of codes runing'''
import timeit
setupCode='from random import randint'
print('timer start',timeit.default_timer())
stmtCode='''def func():
    list=[]
    for i in range(100000000):
        list.append(randint(1,100000000000000))'''
print(timeit.timeit(setup=setupCode,stmt=stmtCode,number=100))
print('timer end',timeit.default_timer())
