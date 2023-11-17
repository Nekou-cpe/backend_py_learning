'''comprehension'''

#list:
list1=[i**2 for i in range(5)]
print(list1)

#func list:
def fun1(m):
    s=m*2
    return s
list3=[fun1(j) for j in range(10)]
print(list3)

#if else:
list5=[3,9,7,6,5]
list4=[c if c%3==0 else c*2 for c in list5]
print(list4)

#nested comprehension:
list2=[[[k for k in range(1,6)]for m in range(1,4)] for n in range(1,3)] 
print(list2)

#dictionary
list3=['red','green','blue','yellow','black']
dict1={key:value for key,value in zip(list1,list3)}
print(dict1)

#set
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set_using_comp = {var for var in input_list if var % 2 == 0}
print("Output Set using set comprehensions:",set_using_comp)
