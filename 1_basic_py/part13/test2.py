#point: else after a loop is using for test the loop ,that works untill end or not
'''for else'''

print('test 1')
for i in range(10):
    print(i,end=' ')
else:
    print('this loop work to end')

print('test 2')
for j in range(10):
    if j==8:
        break
    print(j,end=' ')
else:
    print('this loop work to end')

'''while else'''

print('test 3')
n=12
while n>0:
    print(n,end=' ')
    n-=2
else:
    print('this loop work to end')

print('test 4')
n=10 
while n>0:
    if n==3:
        break
    print(n,end=' ')
    n-=1
else:
    print('this loop work to end')


