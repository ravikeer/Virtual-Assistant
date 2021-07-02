# craeted date function 
import pyttsx3
import datetime #INBUILTLIBRARYS
import speech_recognition as sr # import speech recognition

eng=pyttsx3.init()

def speak(audio):
    eng.say(audio)
    eng.runAndWait()


def getvoices(voice): #NOT CALLING THIS FUNCTION IN THIS FILE
    voices=eng.getProperty('voices')
   # print(voices[1].id)  to know which voice it contain o for male 1 for female
    if voice==1:
       eng.setProperty('voice',voices[0].id)
       speak("hello this is jarvis!")

    if voice==2:
       eng.setProperty('voice',voices[1].id)
       speak("hello this is friday")
    

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

def takecommandMic(): #take command from mic
    r = sr.Recognizer()
    with sr.Microphone() as source: #store our specch in source var iit will also nable microphone
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)  #store our audio speech in audio

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-IN") # convert our speech to text in english india
        print(query)

    except Exception as e: #if not able to recognize
        print(e) # if any error display error
        speak("Say that again please...")
        return "None"   #returning none string

    return query # return query to display for time or date or any command



def takecommandcmd():
    query=input("please tell me how can i help you!\n")
    return query


#calling mic function inside main
if __name__=="__main__": #syntax of main function
    getvoices(1)
    wishme()  #calling wishme function
    while True:
        query=takecommandMic().lower() # calling command function to get query to convert all char to lower case
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