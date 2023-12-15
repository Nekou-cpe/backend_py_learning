
class Iterable:
    def __init__(self,listt) -> None:
        self.listt=listt
        self.itlistt=iter(self.listt)
    
    def __iter__(self):
        return self.itlistt
    
    def __call__(self):
        return next(self.itlistt)
    
listt=Iterable([1,2,3,45,6,67])
#type 1 
itlist=iter(listt)
for i in itlist:
    print(i)
#type 2
itlist2=iter(listt,45)
for j in itlist2:
    print(j)