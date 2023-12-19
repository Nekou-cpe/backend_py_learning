'''Generators: is a function reaturn iterator object by using yeild keyword'''
def generator1(x,y):
    yield x+y
    yield x-y
    yield x*y
    yield x//y

for obj in range(3):
    print(generator1(20,5))

for item in generator1(20,5):
    print(item)

list1=list[generator1(30,3)]
print(list1)
list1=list(generator1(30,3))
print(list1)

set1=set(k for k in generator1(100,5))
print(set1)

'''now i creat two things :first a list
secound a generator, you can see generator help me
to use less memory and time'''
list2=[j for j in range(1,10000)]
print(list2[0:8])
#creating generator in one line
obj2=(x for x in range(1,10000))
for x in range(0,8):
    print(next(obj2),end=',')
