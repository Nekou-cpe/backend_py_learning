'''operator module'''
import operator
#+ - * / // %
print(operator.add(34,5))
print(operator.sub(34,5))
print(operator.mul(34,5))
print(operator.truediv(34,5))
print(operator.floordiv(34,5))
print(operator.mod(34,5))
# == <= >= < >
print(operator.le(4,5))
print(operator.le(5,5))
print(operator.le(7,5))
print()
print(operator.ge(34,5))
print(operator.ge(5,5))
print(operator.ge(4,5))
print()
print(operator.eq(34,5))
print(operator.eq(5,5))
print()
print(operator.lt(34,5))
print(operator.lt(5,5))
print(operator.lt(4,5))
print()
print(operator.gt(34,5))
print(operator.gt(4,5))
print(operator.gt(5,5))
print()
#not
print(operator.not_(False))
print(operator.not_(operator.lt(55,6)))
print()
#left shift binary lshift, right shift binary rshift
print(operator.rshift(8,1))
print(operator.lshift(4,1))
print()
#the iterable obj contains x
list1=[1,2,33,10,4,3,65,243,10,878,10]
print(operator.contains(list1,1))
print(operator.contains(list1,23))
#the iterable obj count of x
print(operator.countOf(list1,10))
#the iterable obj del item of index x
operator.delitem(list1,2)
print(list1)
#the iterable obj getter item x
list2=[('Neko','Dfrm',20),('Nikolj','Dfrm',34),('Sara',"schwester",12)]
print(operator.itemgetter(1)(list2))
print(operator.itemgetter(2)(list1))
print(sorted(list2,key=operator.itemgetter(2)))