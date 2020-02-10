


from tkinter import *
from tkinter import messagebox
 
top=Tk()
l1=Label(top,text="username")
l2=Label(top,text="password")
l3=Label(top,text="username")
l4=Label(top,text="password")
l1.grid(column=0,row=1)
l2.grid(column=2,row=1)
l3.grid(column=4,row=1)
l4.grid(column=6,row=1)

e1=Entry(top,bd=5)
e1.grid(column=1,row=0)
e2=Entry(top,bd=5)
e2.grid(column=3,row=0)
e3=Entry(top,bd=5)
e3.grid(column=5,row=0)
e4=Entry(top,bd=5)
e4.grid(column=7,row=0)
def submit() :
 messagebox.showinfo( "CONFIRMATION",e1.get() +" - Your Data")
redbutton=Button(top,text="nazim BUTTON",fg="green" ,command=submit)
redbutton.grid(column=6,row=5)
top.mainloop()

