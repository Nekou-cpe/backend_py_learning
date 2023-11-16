'''Error Types:
#first we want to learn how many Error Python has

a=2 
b=0 
print(a/b)#zerodivisionError

a='23a2'
print(int(a))#typeError

a=[1,2,3]
print(a[4])#indexError

for i in range(1,20):
     print(i)#indatationError->syntaxError

print(Nekou)#NameError

open(file.txt,'r')#filenotfoundError

RuntimeError->user doesnt fallow ther rules ,rules writes by programmer
'''
'''Exception handeling 1)'''

try:
    a=int(input('first number : '))
    b=int(input('second number : '))
    print(a/b)
except ZeroDivisionError as error:
    print(error)
else:
    print('this is your division number')
finally:
    print('the end...')