# craeted multiple input text anf voice change
import pyttsx3

eng=pyttsx3.init()

def speak(audio):
    eng.say(audio)
    eng.runAndWait()


def getvoices(voice,audio):
    voices=eng.getProperty('voices')
   # print(voices[1].id)  to know which voice it contain o for male 1 for female
    if voice==1:
       eng.setProperty('voice',voices[0].id)

    if voice==2:
       eng.setProperty('voice',voices[1].id)

    speak(audio)

while (True):
    voice=int(input("press 1 for male voice\n press 2 for female voice\n"))
    audio=input("enter the text to convert to speech\n") #taking input from user

    getvoices(voice,audio)
#while(True):   #taking multiple input from user
     #audio=input("enter the text to convert to speech\n") #taking input from user
     #speak(audio) #calling speak function