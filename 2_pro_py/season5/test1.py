'''iterable-> the things can iterator
iterable such as: list , str ,set ,...
iterator such as : min max sum avg ,...
'''
#these can be iterable:
list1=[12,4,3,5,66]
iter(list1)
str1='Nekou'
iter(str1)
#but it does not iterable
#int1=112
#iter(int1)

#work with iterators
def iterOrNot(something):
    try:
        iter(something)
        return True
    except:
        return False
    
class Person:
    def __init__(self,name,fname) -> None:
        self.name=name
        self.fname=fname
    def __str__(self) -> str:
        return f'{self.name},{self.fname}'
    
person1=Person('Nekou','Dfrm')
person2=Person('Nikolj','Dfrm')
people_list=[person1,person2]
print(iterOrNot(people_list))

#for loop on itrators
itlist1=iter(list1)
for i in range(len(list1)):
    print(next(itlist1)) #using next for go to next iter