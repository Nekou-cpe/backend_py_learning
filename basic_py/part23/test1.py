'''useful function2: str functions:
title    join   split   lower   upper   len startswith   
strip   rjust ljust  center isdigit  endswith    isnumeric
point: isdigit and isnumeric are same, the diffrenc between them is
isnumeric can indentify unic codes too'''

#upper case the title
name='nekou'
print(name.title())
#list to str
list1=['it','is','me','20','years','old']
str1=' '.join(list1)
print(str1)
#split with item in str
list2=str1.split(' ')
print(list2)
#upper and lower case all in str ...
str2='   i realy love my self   '
str3=str2.upper()
str4=str3.lower()
print(str3,'\n',str4)
#len of everything
print(len(list1))
#start or and with what?
print(str4.startswith('i'))
print(str4.endswith('i'))

print('*'+str3.rjust(30,' ')+'*')
print('*'+str3.ljust(30,' ')+'*')
print('*'+str3.center(30,'*')+'*')
#is it digit or not?
print('87'.isdigit(),'\n','87'.isnumeric())
#delet space start and end
print(str2.strip(),'*')

