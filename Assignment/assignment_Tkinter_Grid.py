"""
Registration Form
Entries - Username, Mobile, E-Mail, Age, Password, Password 2
2 Buttons - Login, Cancel
"""
from tkinter import *
root=Tk()

l1=Label(root,text="Username")
l2=Label(root,text="Mobile")
l3=Label(root,text="E-Mail ID")
l4=Label(root,text="Age")
l5=Label(root,text="Password")
l6=Label(root,text="Re-Enter Password")

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)
entry5=Entry(root)
entry6=Entry(root)

but1=Button(root,text="Login")
but2=Button(root,text="Cancel")

l1.grid(row=0,column=0)
entry1.grid(row=0, column=1)

l2.grid(row=1,column=0)
entry2.grid(row=1, column=1)

l3.grid(row=2,column=0)
entry3.grid(row=2, column=1)

l4.grid(row=4,column=0)
entry4.grid(row=4, column=1)

l5.grid(row=5,column=0)
entry5.grid(row=5, column=1)

l6.grid(row=6,column=0)
entry6.grid(row=6, column=1)

but1.grid(row=7,column=0)
but2.grid(row=7,column=1)

mainloop()