'''itertools module:
you can work with iterables easier
'''
import itertools
import operator
print(dir(itertools))
#count  from 10 start and then 10 by 10 go then
for i in itertools.count(10,10):
    if i>1000:
        break
    print(i,end=' ')
print('---------------1')
#cycle 
count=0
list1=['ads','bfds','cdfad','ddfa']
for j in itertools.cycle(list1):
    if count>100:
        break
    print(j,end=' ')
    count+=1
print('---------------2')
#repeat
sting1='Hello World'
for k in itertools.repeat(sting1,3):
    print(k,end='*')
print('---------------3')
'''for working in data you can use:
combinations,permytations,product'''    
#the next things are using for recursive or order or combination
#product -> mul matrixs
list2=[1,2,3]
list3=list(itertools.product(list1,repeat=2))
list4=list(itertools.product(list1,list2))
print(list3)
print(list4)
#permutations: can changing places
list5=list(itertools.permutations(list2,3))
#combinations: no chaging places
list6=list(itertools.combinations(list2,3))
print(list5)
print(list6)
print('---------------4')
'''for math thing is good to know :
accumulate'''
list7=[10,9,8,7]
list8=list(itertools.accumulate(list7,operator.sub))
list9=list(itertools.accumulate(list7))
print(list8)
print(list9)
print('---------------5')
#chain using by set structures,they should be iterable:
list10=list(itertools.chain.from_iterable([list1,list2,sting1,list7]))
print(list10)
#compress
list11=list(itertools.compress(sting1,[0,1,1,0,0,0,1,1,0,0]))
print(list11)
#dropwhile -> first parametr should be lambda func or func,second should be iterable ->it shows after that condition not true
list12=[3,1,2,3,4,5,6,7,8,9,10]
list13=list(itertools.dropwhile(lambda x: x*2>4,list12))
#filterfalse -> shows the things are not except condition
list14=list(itertools.filterfalse(lambda x: x*2>4,list12))
#takewhile -> not dropwhile
list15=list(itertools.takewhile(lambda x: x*2>4,list12))
print(list13)
print(list14)
print(list15)
# works like slicing, but for any iterable (not just lists). It returns a slice from the iterable
#list7[1:3:2]
list16=list(itertools.islice(list7,1,3,2))
print(list16)