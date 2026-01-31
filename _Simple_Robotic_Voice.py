import time
import pyttsx3
engine = pyttsx3.init()
now = time.time()

speed_dic = {
    "fast": 250,
    "regular": 200,
    "slow":150
}

speed = speed_dic['fast']

engine.setProperty('rate', speed)  
engine.setProperty('volume', 1)  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

f = open("readme.txt") #if there are any quotations in the text it will fail
text_list = f.readlines()
this_text = "".join(txt.replace("\n", " ") for txt in text_list)

print("speed: ", speed)
engine.say(this_text)
engine.runAndWait()

print("Seconds: ",now - time.time())


