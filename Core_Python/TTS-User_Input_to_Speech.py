from tkinter import *
from gtts import gTTS
import os

root=Tk()
canvas=Canvas(root, width=400, height=400) # Total Canvas Size
canvas.pack()

def texttospeech():
    text=entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('output2.mp4')
    os.system('start output2.mp4')

entry=Entry(root)
canvas.create_window(200,100,window=entry) # x and Y points for the center of the entry box
button=Button(text="Start", command=texttospeech)
canvas.create_window(200,150,window=button)

root.mainloop()
