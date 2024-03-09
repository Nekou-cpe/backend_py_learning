"""timer"""
from tkinter import *
c=0
def timer(lablell):
    def counter():
        global c
        lablell.config(text=f'{c}')
        c+=1
        lablell.after(1000,counter)
    counter()
def stop(labell):
    global c
    lablel1.config(text=f'{c}')
def reset(labell):
    global c
    c=0
    lablel1.config(text=f'{c}')
root=Tk()
root.title('timer')
root.iconbitmap('icon/p3.ico')
w=500
h=300
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h,x,y))

lablel1=Label(master=root,text='0',font=('Arial',50),bg='#E782EB')
lablel1.pack()

button1=Button(master=root,text='start',width='30',font=('Arial',20))
button2=Button(master=root,text='stop',width='30',font=('Arial',20))
button3=Button(master=root,text='reson',width='30',font=('Arial',20))
button4=Button(master=root,text='restart',width='30',font=('Arial',20))
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button1.bind("<Button>",timer(lablel1))
button2.bind("<Button>",stop(lablel1))
button3.bind("<Button>",timer(lablel1))
button4.bind("<Button>",reset(lablel1))


root.mainloop()