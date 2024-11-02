def printer(str1):
    return str1[start]

chop=iter(lambda: printer(str1),'')#beacaus we have iter then non stop keeping this lambda working
str1='hello world'
start=0
for item in chop:
    print(item)
    start+=1
    try:
        if start==len(str1):
            break
    except IndexError as error:
        print(error)
    