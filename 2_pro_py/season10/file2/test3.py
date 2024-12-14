import os
class FileWritable:
    def __init__(self,filePath):
        self.filePath=filePath
        
    def __enter__(self):
        self.fileObject=open(self.filePath,'a+')
        return self.fileObject
    def __exit__(self,*exc):
        if(self.fileObject):
            self.fileObject.close()
        return False
os.chdir('D:/backend_dev/darsman_py/2_pro_py/season10/file2')

with FileWritable('test2.txt') as f1:
    f1.write('welcome to python . hello.', '\t')