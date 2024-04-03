#many thread managing
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def func(name,family):
    print('start',name,' ',family)
    sleep(4)
    print('End',name,' ',family)

with ThreadPoolExecutor(max_workers=2) as executer: #controling many of threads
    names=['Nekou','Nikol','Sara','Bruno']
    familys=['Dfrm','Dfrm','schwester','schwester']
    executer.map(func,names,familys)
    