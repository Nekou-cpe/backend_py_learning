from threading import Timer,current_thread
from time import sleep

def func1(name):
    print(current_thread().name)
    sleep(2)
    print(name)
    
t1=Timer(5,func1,args=['Neko'])
t1.start()
t1.join()
print('the end')