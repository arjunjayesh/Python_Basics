import parser
from tkinter import *
root=Tk()

root.title("Calculator")

display=Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i=0
def get_num(num): # Get the User Input and place it in the text field
    global i
    display.insert(i,num)
    i+=1

def clear_all(): # Clear the entire text field
    display.delete(0,END)

def backspace(): # Clear the last character from the text field
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def get_operator(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entire_sting=display.get()
    try:
        a=parser.expr(entire_sting).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

# Numbers
Button(root,text="0",command=lambda :get_num(0)).grid(row=5, column=0)
Button(root,text="1",command=lambda :get_num(1)).grid(row=4, column=0)
Button(root,text="2",command=lambda :get_num(2)).grid(row=4, column=1)
Button(root,text="3",command=lambda :get_num(3)).grid(row=4, column=2)
Button(root,text="4",command=lambda :get_num(4)).grid(row=3, column=0)
Button(root,text="5",command=lambda :get_num(5)).grid(row=3, column=1)
Button(root,text="6",command=lambda :get_num(6)).grid(row=3, column=2)
Button(root,text="7",command=lambda :get_num(7)).grid(row=2, column=0)
Button(root,text="8",command=lambda :get_num(8)).grid(row=2, column=1)
Button(root,text="9",command=lambda :get_num(9)).grid(row=2, column=2)

Button(root,text="(", command=lambda :get_operator('(')).grid(row=5, column=1)
Button(root,text=")", command=lambda :get_operator(')')).grid(row=5, column=2)

Button(root,text="pi", command=lambda :get_operator('3.14')).grid(row=2, column=3)

Button(root,text="+", command=lambda :get_operator('+')).grid(row=3, column=3)
Button(root,text="*", command=lambda :get_operator('*')).grid(row=4, column=3)
Button(root,text="-", command=lambda :get_operator('-')).grid(row=3, column=4)
Button(root,text="/", command=lambda :get_operator('/')).grid(row=4, column=4)

Button(root,text="AC", command=clear_all).grid(row=5, column=3)
Button(root,text="<-", command= lambda :backspace()).grid(row=2, column=4)

Button(root,text="=", command=lambda :calculate()).grid(row=5, column=4)

root.mainloop()