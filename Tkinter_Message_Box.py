from tkinter import *
from tkinter import messagebox
root=Tk()

messagebox.showinfo('Title',"This is my Info")
messagebox.showwarning('Title',"This is my Warning")
messagebox.showerror('Title',"This is my Error")

messagebox.askquestion('title',"Are you Sure")
messagebox.askokcancel('title',"Are you Sure")
messagebox.askyesno('title',"Are you Sure")
messagebox.askretrycancel('title',"Are you Sure")

root.mainloop()
