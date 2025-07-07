import re
# match method ->search about it
str1=" niko nikol sara maria aria sam"
re_search=re.search(r'\sn\w*',str1) #search return first result
re_findall=re.findall(r'\sn\w*',str1)#finding all
print(re_search)#object address
print(re_search.group())# object to str for print
print(re_findall)

#finding true numbers:
phone_list=['0249876543212 0049000000000 0049872222222222222222222222 0049896543212 004987654 004987aa43212 0049555555555 ']
re_phon=re.findall(r'(0049\d{9})\s',' '.join(phone_list))
print(re_phon)

#finding true gmail
gmail_list='nikjflsaf@gmail.com  aaaaaaaaaf@gmail.com  dddddddddddd@gmail.com 9778768djjf@gmail.ir  jgfljs.com fjsl@gail.co'
re_gmail=re.findall(r'[a-zA-Z]+\@.+\..{2,3}',gmail_list)
print(re_gmail)

#new test
str_list='''
Name is : Nekou , Age is : 22 , Avrg : 96
Name is : Nikol , Age is : 21 , Avrg : 70.5
Name is : Nanami , Age is : 50 , Avrg : 67
Name is : Nikolas , Age is : 30 , Avrg : 70
Name is : Maria , Age is : 31 , Avrg : 94
'''
re_str=re.findall(r'Name is : (\w+) , Age is : (\d+) , Avrg : (\d+\.\d*)',str_list)
print(re_str)
#re.sub->replace
re_str_sub=re.sub(r'Name is : (\w+) , Age is : (\d+) , Avrg : (\d+\.*\d)','\g<1> , \g<2> , \g<3>',str_list)
print(re_str_sub)