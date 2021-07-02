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


def greeting(): #will greet good morning or any by seeing time
    hour=datetime.datetime.now().hour #getting hr
    if hour>=6 and hour<12:
       speak("good morning sir!")

    elif hour>=12 and hour<16:
       speak("good afternoon sir!")

    elif hour>=16 and hour<24:
       speak("good evening sir!")

    else:
      speak("good night sir!")

def wishme():
    speak("welcome back ravi!")
    time()# calling time function
    date()#calling date function
    greeting() #calling greeting function
    speak("jarvis at your service, please tell me how can i help you!")


def takecommandcmd():
    query=input("please tell me how can i help you!\n")
    return query

if __name__=="__main__": #syntax of main function
    wishme()  #calling wishme function
    while True:
        query=takecommandcmd().lower() # calling command function to get query to convert all char to lower case
        if 'time' in query:
            time()

        elif 'date' in query:
            date()





#while (True):
    #voice=int(input("press 1 for male voice\n press 2 for female voice\n"))
    #audio=input("enter the text to convert to speech\n") #taking input from user

    #getvoices(voice,audio)
#while(True):   #taking multiple input from user
     #audio=input("enter the text to convert to speech\n") #taking input from user
     #speak(audio) #calling speak function