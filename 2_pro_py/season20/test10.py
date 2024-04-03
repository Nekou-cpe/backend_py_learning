#semaphore
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from threading import Thread,current_thread,Semaphore

num=0
lock=Semaphore(value=2)
def numCounter1():
    global num
    lock.acquire()#Stop other threads for this source
    num+=1
    sleep(1)
    print(f'counter{current_thread().name} , {num}')
    lock.release()#share source 
    #lock.release()#cant error when you use wrong semaphore methods


thread_list=[]
for i in range(10):
    thread_list.append(Thread(target=numCounter1))

for i in range(10):
    thread_list[i].start()

for i in range(10):    
    thread_list[i].join()

print(f'counter{current_thread().name} , {num}')
print('the end')
    
    
    
    
    