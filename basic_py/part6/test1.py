'''print'''
#end= sep=
print('hello',end='_')
print('world')
print('my','name','is',sep='-')

#control str \n \t
print('hello \t world \nyeeee')

#remove control characters
print(r'hello\ni realy love \t python')

#format
fname='Neko'
lname='Dfrm'
age=20
print(f'my name is: {fname}\t my last name is: {lname}\ni\'m {age} years old')
print('name {} last name {} age {}'.format(fname,lname,age))