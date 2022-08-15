from tkinter import *
root=Tk()

def fun1():
    print("Clicked")

mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="Save")
submenu.add_command(label="Save1")
submenu.add_separator()
submenu.add_command(label="Save")
submenu.add_command(label="Save")

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="undo", command=fun1)

toolbar=Frame(root, bg="pink")
toolbar.pack(side=TOP,fill=X)
inbutton=Button(toolbar,text="Crop")
inbutton.pack(side=LEFT,padx=5, pady=5)

statusbar=Label(root,text="This is a Status Bar",bd=2, relief='sunken')
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()