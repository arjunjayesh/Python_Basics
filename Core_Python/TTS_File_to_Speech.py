from gtts import gTTS
import os

text=open("TTS_demo.txt",'r', encoding='utf-8').read()

output=gTTS(text=text, lang='en', slow=False)
output.save('output1.mp3')
os.system('start output1.mp3')