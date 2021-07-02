# craeted date function 
import pyttsx3
import datetime #INBUILTLIBRARYS

eng=pyttsx3.init()

def speak(audio):
    eng.say(audio)
    eng.runAndWait()


def getvoices(voice,audio): #NOT CALLING THIS FUNCTION IN THIS FILE
    voices=eng.getProperty('voices')
   # print(voices[1].id)  to know which voice it contain o for male 1 for female
    if voice==1:
       eng.setProperty('voice',voices[0].id)

    if voice==2:
       eng.setProperty('voice',voices[1].id)

    speak(audio)

def time(): #not calling this function
    time=datetime.datetime.now().strftime("%I:%M:%S") #I FOR HOUR M FOR MINUTE S FOR SECOND
    speak("current time is")
    speak(time)


def date():
    year=int(datetime.datetime.now().year) #get currnt year
    month=int(datetime.datetime.now().month) #get current month
    date=int(datetime.datetime.now().day)
    speak("current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back ravi!")
    time()# calling time function
    date()#calling date function
    speak("jarvis at your service, please tell me how can i help you!")

wishme()





#while (True):
    #voice=int(input("press 1 for male voice\n press 2 for female voice\n"))
    #audio=input("enter the text to convert to speech\n") #taking input from user

    #getvoices(voice,audio)
#while(True):   #taking multiple input from user
     #audio=input("enter the text to convert to speech\n") #taking input from user
     #speak(audio) #calling speak function