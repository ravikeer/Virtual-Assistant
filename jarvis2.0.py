import pyttsx3

eng=pyttsx3.init()

def speak(audio):
    eng.say(audio)
    eng.runAndWait()


while(True):   #taking multiple input from user
     audio=input("enter the text to convert to speech\n") #taking input from user
     speak(audio) #calling speak function