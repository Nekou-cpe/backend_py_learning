from time import sleep
from threading import Thread

def func(name):
    print('start',name)
    sleep(6)#example of complex programm
    print('stop',name)

#creating thread
Thread1=Thread(target=func,args=['Nekou'])#args is list or set
Thread2=Thread(target=func,args=['Nekol'])
#calling thread for work
Thread1.start()
Thread2.start()
print('the end...')
