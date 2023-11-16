'''Exception handeling 1)'''
try:
    a=int(input('first number : '))
    b=int(input('second number : '))
    print(a/b)
    
    c=[i for i in range(1,10)]
    d=int(input('which index in list ? '))
    print(c[d])

except ZeroDivisionError as error:
    print(error)

except TypeError as error:
    print(error)

except IndexError as error:
    print(error)

except ValueError as error:
    print(error)
    
finally:
    print('the end...')