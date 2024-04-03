from time import sleep
from threading import Thread

def func(name):
    print('thread start',name)
    sleep(5)    
    print('thread done',name)

t1=Thread(target=func,args=['Nekou'],daemon=True)
t2=Thread(target=func,args=['Nikol'],daemon=True)#cant use join for daemon True thread
t1.start()
t2.start()
print('the end')
