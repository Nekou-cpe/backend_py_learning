'''In Python, the __call__() method is used to make an object 
callable like a function. When you define a class in Python, you 
can define the __call__() method to make the instances of the class 
callable. This means that you can use the instance of the class like 
a function and call it with arguments.'''
class Iterable():
    def __init__(self,listt) -> None:
        self.listt=listt
        self.itlistt=iter(self.listt)
    
    def __iter__(self):
        try:
            self.itlistt=iter(self.listt)
            return self.itlistt
        except:
            print('not iterable')
            
    
    def __call__(self):
        return next(self.itlistt)
    
listt1=Iterable([1,2,3,45,6,67])
listt2=Iterable([7,8,9,10])
#type 1 
itlist=iter(listt1)
for i in itlist:
    print(i)
print('--------')
#type 2
itlist2=iter(listt2,10)
for j in itlist2:
    print(j)