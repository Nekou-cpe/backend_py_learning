import os
'''file object:
methods: tell()-> where are you now in file seek()-> jump to 
attributes: mode , name ,close'''
#rb-> read binary
print(os.chdir('d:/backend_dev/darsman_py/2_pro_py/season10/file1/'))
file1=open('test1.txt','rb')
print(file1.tell())
print(file1.readline())
file1.seek(10,0)
print(file1.readline())
file1.seek(-10,2)
file1.write('***')
print(file1.tell())
print(file1.name)
print(file1.mode)
print(file1.closed)
file1.close()
print(file1.closed)