class MyClass():
    _counter=0
    def __init__(self,color):
        self.color=color
    @staticmethod
    def great(name):
        return f'hello {name}'

    @classmethod
    def howmany(cls):
        cls._counter+=1
        return f'counting obj {cls._counter}'

obj1=MyClass('pink')
obj2=MyClass('yellow')
obj3=MyClass('pink')
obj4=MyClass('pink')
print(MyClass.great('Nekou'))
print(MyClass.howmany())
print(MyClass.howmany())
