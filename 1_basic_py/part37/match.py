#match case basic
num='niko'
match num:
    case 'niko':
        print('niko')
    case _:
        print('num is not niko')