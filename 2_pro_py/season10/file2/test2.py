'''context manager'''
try:
    with open("test1.txt",'r') as  f1, open('''test2.txt''','r+') as f2:
        print(f1.read())
        for line in f1.readlines():
            f2.write(line)
        print('-----------------')
        print(f2.read())
except Exception as error:
    print('Error: ',error)
finally:
    print('The end...')
    f1.close()
    f2.close()
    print(f1.closed)