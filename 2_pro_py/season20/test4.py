from time import sleep
from threading import Thread,current_thread

def func(name):
    print('thread start',name)
    print(current_thread().name)
    sleep(5)    
    print('thread done',name)

t1=Thread(target=func,args=['Nekou'])
t2=Thread(target=func,args=['Nikol'])
t1.start()
t2.start()

t1.join()
t2.join()
print(current_thread().ident)
print('the end')
