class Person:
    def __init__(self,name , code) -> None:
        self.code=code
        self.name=name
        
    def __enter__(self):
        print('starting')
        return self
    
    def __exit__(self,*exc):
        print('finishing')
        return False
    
    def getCode(self):
        return self.code
    
with Person('neko',209045) as person1:
    print(person1.getCode())
