from tkinter import *
class Test:
    def __init__(self,rootone):

        frame=Frame(rootone)
        frame.pack()

        self.pbutton=Button(frame,text='Click', command=self.pmsg)
        self.pbutton.pack(side=LEFT)

        self.qbutton=Button(frame,text='Cancel', command=self.qmsg)
        self.qbutton.pack(side=LEFT)

        self.rbutton=Button(frame,text="exit", command=frame.quit)
        self.rbutton.pack(side=LEFT)

    def pmsg(self):
        print("Clicked")

    def qmsg(self):
        print("Cancelled")

root=Tk()
obj=Test(root)
root.mainloop()