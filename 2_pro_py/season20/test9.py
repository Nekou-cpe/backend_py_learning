#many thread managing
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from threading import Thread,current_thread,RLock

num=0
lock=RLock()
def numCounter1():
    global num
    lock.acquire()#Stop other threads for this source
    numCounter2()
    num+=1
    sleep(1)
    print(f'counter{current_thread().name} , {num}')
    lock.release()#share source 

def numCounter2():
    global num
    lock.acquire()#Stop other threads for this source
    num-=1
    sleep(1)
    print(f'counter{current_thread().name} , {num}')
    lock.release()#share source   
t1=Thread(target=numCounter1)
t2=Thread(target=numCounter1)

t1.start()
t2.start()
    
t1.join()
t2.join()

print(f'counter{current_thread().name} , {num}')
print('the end')
    
    
    
    
    