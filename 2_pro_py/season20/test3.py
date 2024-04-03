from time import sleep
from threading import Thread,enumerate
def func(name):
    print('thread start',name)
    print(enumerate())
    sleep(5)    
    print('thread done',name)

t1=Thread(target=func,args=['Nekou'])
t2=Thread(target=func,args=['Nikol'])
t1.start()
t2.start()

t1.join()
t2.join()
print(enumerate())
print('the end')
