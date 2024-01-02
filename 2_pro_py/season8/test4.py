'''collection -> for big data
you can creat news structures'''
import collections
list1=[1,23,22,45,4,56,5,4,78,4]
print(collections.Counter(list1))
a='ajfd;k;sdfoiugioueiorufoqwj;ehfo;hovnfksdjklfklshad;fj'
print(collections.Counter(a))
print(collections.Counter(a).most_common(3))
'''this has error
dict1={}
dict1['h']=5'''
#this way has no error type: int str object-> it means you can give dict any type
dict1=collections.defaultdict(object)
print(dict1) #has no error
dict1['h']=5
dict1['m']='hello'
dict1[3]='hi'
dict1[2]=6
print(dict1) #has no error
print()
dict2={'a':'b','c':'d','h':'g'}
dict3={'c':'d','h':'g','a':'b'}
print(dict2==dict3)
#but sometimes order is important so:
dict4=collections.OrderedDict({'a':'b','c':'d','h':'g'})
dict5=collections.OrderedDict({'h':'g','c':'d','a':'b'})
print(dict4==dict5)
print()
#chainmap-> steak all dict together
dict6=collections.ChainMap(dict1,dict2,dict3,dict4,dict5)
print(dict6)
print()
#namedtuple -> is new structure you can work it when you need class obj with attribut
People=collections.namedtuple('People', 'name age code_indentify number children')
person1=People('Nekou',21,4889,848974298,[])
person2=People('Nikolj',35,758983,14341,['a','b'])
print(person1)
print(person2)
print(person1.age)
print(person1.children)
print(person2.name)
#People._make(person2)-> make person2 itrable then doestn show attribute names,...
for item in People._make(person2):
    print(item)
#person1._asdict -> return to dict
print(person1._asdict())
#person1._fields ->return filds in obj
print(person1._fields)
print()
#you can creat queue of stack with new structure:
dqu1=collections.deque(['a','b','c','d','h'])
print(dqu1)
dqu1.append('m')
print(dqu1)
dqu1.appendleft('0')
print(dqu1)
dqu1.pop()
print(dqu1)
dqu1.popleft()
print(dqu1)
#UserString,UserList,UserDict -> for working on these object class
#search for these
