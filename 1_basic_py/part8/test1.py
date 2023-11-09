'''
condition
1)if else elif
'''
number=int(input('write your score in this course'))
if number<0 or number>20:
    print('Eror')
elif number>12:
    print('you pass ')
else:
    print('you fail')