'''nested loop'''
for i in range(5):
    for j in range(1,3):
        if i%j==0:
            print(f'i is :{i}, j is {j}')
        else:
            print('i%j was not zero')