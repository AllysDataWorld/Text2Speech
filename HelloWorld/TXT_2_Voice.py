
import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
new_rate = rate + 10
engine.setProperty('rate', new_rate)  
engine.setProperty('volume', 1)  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print("rate ", new_rate)
engine.say("Hello world")
engine.runAndWait()