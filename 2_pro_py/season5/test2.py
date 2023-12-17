'''itrators: sum , min , max , sorted , 
enumerate -> show index of data behind of that 
,any-> any of set are true will be true
,all-> should all of the set be true'''

class Fibonatchi:
    def __init__(self,end) -> None:
        self.a=0
        self.b=1
        self.end=end

    def __iter__(self):#object to iterable object
        return self
    
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>self.end:
            raise StopIteration('Stop Iteration')
        return self.a
    
fib1=Fibonatchi(7240927349)
for i in fib1:
    print(i)

#all,any
list1=[True,True,False]
list2=[True,True,True]
list3=[False,False,False]
print(all(list1))
print(all(list2))
print(all(list3))
print(any(list1))
print(any(list2))
print(any(list3))