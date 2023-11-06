'''lambda'''

#basic lambda
def fun(x):
    return 2*x

print(fun(8))

print((lambda x:x*2)(5))

#lambda in one line
print((lambda m,n,functionOther:functionOther(m,n))(23,12,lambda num1,num2:num1*num2))

#mixing lambda and sorted
courses=['math202','math102','physic101','physic100','algorithem116']
print(sorted(courses,key=lambda q:q[1:]))
