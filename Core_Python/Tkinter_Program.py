from tkinter import *
root=Tk()

# Label
label=Label(root,text="Hello World").pack()
frame1=Frame(root)
frame1.pack()

# Button
but=Button(root,text="Login",fg="red",bg="black")
but.pack()


root.mainloop()
