''' the *exc parameter is used to catch any 
exception that might occur in the with block'''
class Files:
    def __init__(self,file,file_mode) -> None:
        self.file=file
        self.file_mode=file_mode
        
    def __enter__(self):
        print('starting')
        self.obj_file=open(self.file,self.file_mode)
        return self.obj_file
    
    def __exit__(self,*exc):#exc -> all exception we can write here
        print('finishing')
        if(self.obj_file):
            self.obj_file.close()
            
        for e in exc:
            print(e)
            
        return False 
#enter and exit works with context manager in class 
with Files("test1.txt",'w') as f1:
    f1.write('hello world \n')  
    f1.write('Nekou \n') 
    
