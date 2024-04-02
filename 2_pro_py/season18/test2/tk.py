from tkinter import *
from tkinter import messagebox

def func1():
    label1.config(text='Age calculator')
def pressed(event):
    entry=int(entry1.get())
    n=entry+300
    messagebox.showinfo('your age is',str(n))
root=Tk()
root.title('Python first test')
#root.iconbitmap('icon/p3.ico')
w=700
h=500
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
frame1=Frame(root,width='700',height='200',bg='#FFCCE5')
frame2=Frame(master=root,width='700',height='400',bg='#E782EB')

label1=Label(master=frame1,
             text='welcome',
             font=('Script',30,'bold'),
             width='20',
             height='2')
entry1=Entry(master=frame2,
             bg='#ffccff',
             width='30',
             
             )
button1=Button(master=frame2,text='set',cursor='heart')
button1.bind('<Button>',pressed)

frame1.pack()
frame2.pack()
label1.after(1000,func1)
label1.place(x=200,y=50)
entry1.place(x=300,y=50)
button1.place(x=460,y=50)
root.mainloop()