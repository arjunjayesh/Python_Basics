from tkinter import *
root=Tk()

# pack is not used when using grid

l1=Label(root,text="Username")
l2=Label(root,text="Password")
l3=Label(root,text="Password Again")

entry1=Entry(root) # Input Box
entry2=Entry(root)

l1.grid(row=0,column=0)
entry1.grid(row=0, column=1)
l2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
root.mainloop()
