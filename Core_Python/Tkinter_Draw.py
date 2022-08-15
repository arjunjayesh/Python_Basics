from tkinter import *
root=Tk()

canvas=Canvas(root, width=100, height=200)
canvas.pack()
newline=canvas.create_line(0,0,8,90)
newline1=canvas.create_line(10,10,10,90, fill="green")

root.mainloop()
