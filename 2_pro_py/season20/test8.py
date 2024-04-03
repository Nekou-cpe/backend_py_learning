#many thread managing
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from threading import Thread,current_thread,Lock

num=0
lock=Lock()
def numCounter():
    global num
    with lock:
        num+=1
        sleep(3)
        print(f'counter{current_thread().name} , {num}')
    
t1=Thread(target=numCounter)
t2=Thread(target=numCounter)

t1.start()
t2.start()
    
t1.join()
t2.join()

print(f'counter{current_thread().name} , {num}')
print('the end')
    
    
    
    
    