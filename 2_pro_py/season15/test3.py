from tkinter import *
def func1():
    label1.config(text='Age calculator')
def pressed(event):
    print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))
def move(event):
    print('hello')
root=Tk()
root.title('Python first test')
root.iconbitmap('icon/p3.ico')
root.config(bg='#FFCCE5')
root.resizable(width='0',height='0')
w=700
h=500
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
#root.columnconfigure()
label1=Label(master=root,
             text='welcome',
             font=('Script',30,'bold'))
label2=Label(master=root,
             text='write your birthday',
             bg='#ffccff',
             fg='#000000',
             font='Arial',
             relief=SOLID)
button1=Button(master=label2,text='set',cursor='heart')
button1.bind('<Button>',pressed)
message1=Message(master=root,text="""Hello this is a test for learning
                 everything in tkinter
                 my name is Nekou.""",width=300)

label1.after(1000,func1)
label1.grid(row=1000,column=10)
label2.grid(row=5000,column=100)
button1.place(x='45',y='2')
message1.bind("<Motion>",move)
root.mainloop()