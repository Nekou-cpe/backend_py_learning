import os
import mimetypes
print(os.getcwd())#where is your location in this dir
if not os.path.exists('2_pro_py\\season10\\file3\\file1'):#creat folder anywhere you want
    os.mkdir('2_pro_py\\season10\\file3\\file1')
else:
    print('this folder was created')
print('this way is',os.path.lexists('2_pro_py\\season10\\file3'))#this way is exist?
os.chdir('../')#change dir
print(os.getcwd())
os.chdir('darsman_py\\2_pro_py\\season10\\file3')
print('-------')
print(os.getcwd())
print(os.listdir())#list of dir here
#isdir -> folder   isfile -> file
list_things=os.listdir()
for thing in list_things:
    if os.path.isdir(thing):
        print(f'this is directory: {thing}')
    elif os.path.isfile(thing):
        print(f'this is file: {thing}')
    else:
        print(f'this thing is not folder or file : {thing}')

#methods you should learn 
print(os.path.basename('darsman_py\\2_pro_py\\season10\\file3'))#shows name your file
print(os.path.dirname('darsman_py\\2_pro_py\\season10\\file3'))#show dir without your file
print(os.path.normpath('darsman_py\\2_pro_py\\season10\\file3'))#same as os.getcwd()
print(os.path.realpath('darsman_py\\2_pro_py\\season10\\file3'))#base where is your dir
#size of file ->byte /1024->kb      /1024*1024->mb
print('byte of this file: ',os.path.getsize('test3.py'))
print('kbyte of this file: ',os.path.getsize('test3.py')/1024)
print('mbyte of this file: ',os.path.getsize('test3.py')/(1024*1024))
#getctime->when this file created?by milisec getmtime->time of the last changed
print('when creat this file by days?',os.path.getctime('test3.py')//(60*60*1000*24))
print('last change by days:',(os.path.getmtime('test3.py'))//(60*60*1000*24))
#join thing -> steack together  split->sprate format or file
print(os.path.join('d:\\backend_dev\\','darsman_py','2_pro_py','season10\\file3'))
list_splited_dir=os.path.split('darsman_py\\2_pro_py\\season10\\file3\\text3.py')
print(list_splited_dir)
print(os.path.splitext('darsman_py\\2_pro_py\\season10\\file3\\text3.py'))#split just for format of file
#get mimtypes of any file:
list_format=['test.gz','test2.doc','test4.mp3','test5.pdf','test6.json']
for item in list_format:
    print(f'item:  {item} ,format:  {mimetypes.MimeTypes().guess_type(item)}')
#delete file or folder:
os.rmdir('file1') #Error-> it is not empty
os.rmdir('file1\\file_fortest')#delete empty folder
os.remove('file1\\test.py')#delete file


