'''condition:
    2)match case
    '''
num=int(input('say number between 1 to 3'))

match num:
    case 1:
        print('hi')
    case 2:
        print('hello')
    case 3:
        print('hallo')
    case _:
        print('error')