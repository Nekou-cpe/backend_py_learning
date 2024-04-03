from threading import Event,Thread
from time import sleep

def func1():
    print('thread1 is working...')
    sleep(5)
    print('right time this thread needs somthing from thread2...')
    e1.set()
    e2.wait()
    sleep(10)
    e1.clear()

def func2():
    print('th2 is working')
    sleep(1)
    print('right now thread1 should worke so...')
    e2.set()
    e1.wait()
    sleep(7)
    e2.clear()
    
e1=Event()
e2=Event()

th1=Thread(target=func1)
th2=Thread(target=func2)

th1.start()
th2.start()

print('the end...')