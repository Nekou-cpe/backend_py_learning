'''itertools module:
you can work with iterables easier
'''
import itertools
import operator
print(dir(itertools))
#count 
for i in itertools.count(10,10):
    if i>1000:
        break
    print(i,end=' ')
print('---------------')
#cycle
count=0
list1=['ads','bfds','cdfad','ddfa']
for j in itertools.cycle(list1):
    if count>100:
        break
    print(j,end=' ')
    count+=1
print('---------------')
#repeat
sting1='Hello World'
for k in itertools.repeat(sting1,3):
    print(k,end='*')
print('---------------')
'''for working in data you can use:
combinations,permytations,product'''    
#the next things are using for recursive or order or combination
#product -> mul matrixs
list2=[1,2,3]
list3=list(itertools.product(list1,repeat=2))
list4=list(itertools.product(list1,list2))
print(list3)
print(list4)
#permutations:
list5=list(itertools.permutations(list2,3))
#combinations:
list6=list(itertools.combinations(list2,3))
print('---------------')
'''for math thing is good to know :
accumulate'''
list7=[10,9,8,7]
list8=list(itertools.accumulate(list7,operator.sub))
list9=list(itertools.accumulate(list7))
print(list8)
print(list9)
print('---------------')
#chain using by set structures,they should be iterable:
list10=list(itertools.chain.from_iterable([list1,list2,sting1,list7]))
print(list10)
#compress
list11=list(itertools.compress(sting1,[0,1,1,0,0,0,1,1,0,0]))
print(list11)
#dropwhile -> first parametr should be lambda func or func,second should be iterable
list12=[1,2,3,4,5,6,7,8,9,10]
list13=list(itertools.dropwhile(lambda x: x*2>4,list12))
list14=list(itertools.filterfalse(lambda x: x*2>4,list12))
list15=list(itertools.takewhile(lambda x: x*2>4,list12))
print(list13)
print(list14)
print(list15)
#ist slice
list16=list(itertools.islice(list7,1,3,2))
print(list16)