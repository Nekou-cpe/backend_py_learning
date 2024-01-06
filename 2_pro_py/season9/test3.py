'''recursive function'''
def mul(n,m):
    if n==1:
        return m
    else:
        return m+mul(n-1,m)
        
def fibunatchi(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibunatchi(num-1)+fibunatchi(num-2)
    
list_index=[0,1,2,3,4,5,6,7,8,9,10]
fibo_list=[]
for item in list_index:
    fibo_list.append(fibunatchi(item))
print(fibo_list)

print(mul(4,6))