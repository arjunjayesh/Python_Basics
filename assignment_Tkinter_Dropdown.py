from tkinter import *
root=Tk()

mymenu=Menu(root)
root.config(menu=mymenu)

def f1():
    print("New Project Created")
def f2():
    print("New Scratch File Created")
def f3():
    print("Run the Locate File Dialog Box")
def f4():
    print("Run the Save File Dialog Box")
def f5():
    print("Project Closed")

def e1():
    print("Changes Revoked")
def e2():
    print("Changes Restored")
def e3():
    print("Cut")
def e4():
    print("Copy")
def e5():
    print("Paste")
def e6():
    print("Delete")

file_menu=Menu(mymenu)
mymenu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project", command=f1)
file_menu.add_command(label="New Scratch File")
file_menu.add_separator()
file_menu.add_command(label="Open")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Close Project")
file_menu.add_command(label="Exit", command=file_menu.quit)

edit_menu=Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=e1)
edit_menu.add_command(label="Redo", command=e2)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=e3)
edit_menu.add_command(label="Copy", command=e4)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=e5)
edit_menu.add_command(label="Delete", command=e6)

view_menu=Menu(mymenu)
mymenu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Tool Windows")
view_menu.add_command(label="Appearance")
view_menu.add_separator()
view_menu.add_command(label="Quick Definition")
view_menu.add_command(label="Quick Type Definition")
view_menu.add_separator()
view_menu.add_command(label="Recent Files")
view_menu.add_command(label="Recently Changed Files")

navigate_menu=Menu(mymenu)
mymenu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back")
navigate_menu.add_command(label="Forward")
navigate_menu.add_separator()
navigate_menu.add_command(label="Search Everywhere")
navigate_menu.add_command(label="Class")
navigate_menu.add_separator()
navigate_menu.add_command(label="File")
navigate_menu.add_command(label="Symbol")

code_menu=Menu(mymenu)
mymenu.add_cascade(label="Code", menu=code_menu)
code_menu.add_command(label="Generate")
code_menu.add_command(label="Code Completion")
code_menu.add_separator()
code_menu.add_command(label="Insect Code")
code_menu.add_command(label="Code Cleanup")
code_menu.add_separator()
code_menu.add_command(label="Analyze Code")
code_menu.add_command(label="Analyze Stack Trace or Thread Dump")

refactor_menu=Menu(mymenu)
mymenu.add_cascade(label="Refactor", menu=refactor_menu)
refactor_menu.add_command(label="Refactor This")
refactor_menu.add_command(label="Rename")
refactor_menu.add_separator()
refactor_menu.add_command(label="Change Signature")
refactor_menu.add_command(label="Exact Introduce")
refactor_menu.add_separator()
refactor_menu.add_command(label="Move File")
refactor_menu.add_command(label="Copy File")

root.mainloop()