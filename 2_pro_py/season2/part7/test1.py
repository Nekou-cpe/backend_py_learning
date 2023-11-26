'''instance method -> using these for instance of obj
    static method - > dont call by instance . they use inside class
    class method -> dont call by instance . they can use static method
    why class and static methon? : class is about obj and this obj hase diffrent thing inside itself
    so this uses diffrent methods and attributes'''

class Math():
    lists=[]
    def __init__(self,number,about) -> None:
        self.number=number
        self.about=about

    @staticmethod #this is static method becouse we call staticmethod decoder and it doesnt have *self*
    def sum(x,y):
        return x+y
    
    @classmethod#this is static method becouse we call classmethod decoder and it doesnt have *self* and we write cls
    def mathClass(cls,x):
        Math.lists.append(x)
        return Math.lists

    def __str__(self) -> str:#this is instance method becaus we call attrebute of instance and *self*
        return f'{self.number} , {self.about}'
#instance
Math1=Math(12,'it is 12')
print(Math1)
#how call static and class methods
print(Math.sum(10,12))
print(Math.mathClass(10))
print(Math.mathClass(988))
print(Math.mathClass(546))
