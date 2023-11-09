'''files
w->write
r->read
a->apend
x->creating new file '''
import os #when you want to work in operating system 
file1=open("file1.txt","w")
file1.write("Neko Dfrm\n")
file1.write("bye")
file1.close()

file1=open("file1.txt","r")
#print(file1.read())
print(file1.readlines())
file1.close()

#check this file exist in os -> if this file exist  =true and if this file doesnt exist 
if os.path.exists("file2.txt"):
    print("this file exists")
else : 
    file2=open("file2.txt","x")
    file2.write("Nekou is not Dfrm ")
    file2.close()