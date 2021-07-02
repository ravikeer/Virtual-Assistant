# craeted date function 
import pyttsx3 #for text to speech
import datetime #INBUILTLIBRARYS
import speech_recognition as sr # import speech recognition
import smtplib  #to send email
from secrets import senderemail,pwd #to get username and password as secured
from email.message import EmailMessage #function for email to subject
import pyautogui #for whatsapp
import webbrowser as wb #to open browser for whatsapp
from time import sleep
import wikipedia
import pywhatkit
from newsapi import NewsApiClient #for news update
import clipboard
import requests
import os
import pyjokes
import time as tt #for screenshot as overlapping
import string
import random


eng=pyttsx3.init()

def speak(audio):
    eng.say(audio)
    eng.runAndWait()


def getvoices(voice): #NOT CALLING THIS FUNCTION IN THIS FILE
    voices=eng.getProperty('voices')
   # print(voices[1].id)  to know which voice it contain o for male 1 for female
    if voice==4:
       eng.setProperty('voice',voices[0].id)
       speak("hello this is jarvis!")

    if voice==5:
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

def sendemail(receiver,subject,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,pwd)
    #server.sendmail(senderemail,to,content)
    email=EmailMessage()  #enail is var eprform all operation
    email['From']=senderemail
    email['To']=receiver
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email) #it will send mail
    server.close()

#sendemail()

def whatsmsg(phone_no,message):
    Message=message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak("what should i search for")
    search=takecommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi=NewsApiClient(api_key='894fa9d9513243618e55472db8632f09')
    speak('what topic you need the news about')
    topic=takecommandMic()
    data=newsapi.get_top_headlines(q=topic,language='en',page_size=5)
    newsdata=data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("thats it for now i will update you in a while")

def texttospeech():
    text=clipboard.paste()
    print(text)
    speak(text)
                                         
def covid():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    covid_data=f'confirmed cases:{data["cases"]} \nDeaths:{data["deaths"]} \nRecovered:{data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    speak("taking screenshot")
    name_img=tt.time()
    name_img=f'C:\\Users\\RAVI\\Desktop\\jarvis\\screenshot\\{name_img}.png'
    img=pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    passlen=8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass=("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("okay sir flipping a coin")
    coin=['heads','tails']
    toss=[]
    toss.extend(coin)
    random.shuffle(toss)
    toss=("".join(toss[0]))
    print("i flipped the coin and you got" +toss)
    speak("i flipped the coin and you got"+toss)

#calling mic function inside main
if __name__=="__main__": #syntax of main function
    #val=int(input("press 1 for jarvis mode\npress 2 for friday mode\n"))
    print("say 4 for jarvis mode say 5 for friday mode")
    speak("say 4 for jarvis mode say 5 for friday mode")
    mode=takecommandMic()
    #getvoices(val)
    getvoices(int(mode))
    #wishme()  #calling wishme function
    while True:
        query=takecommandMic().lower() # calling command function to get query to convert all char to lower case
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'email' in query: #to send email from mic
            try:
                email_list= {
                    'test email':'fxm91689@zwoho.com' #10minmail
                }
                speak("to whom should i send")
                name=takecommandMic()
                receiver=email_list[name] #we will get email
                speak("what is the subject")
                subject=takecommandMic()
                speak("what should i say?")
                content=takecommandMic()
                sendemail(receiver,subject,content)
                speak("email has been send")


            except Exception as e:
                print(e)
                speak("unable to send email")

        elif 'message' in query: #to send whatsapp msg
            user_name={
                'Ravi':'+91 ***** *****'
            }
            try:
                speak("to whom should i send message")
                name=takecommandMic()
                phone_no=user_name[name] #we will get email
                speak("what is the message")
                message=takecommandMic()
                whatsmsg(phone_no,message)
                speak("message has been send")


            except Exception as e:
                print(e)
                speak("unable to send message")
        elif 'wikipedia' in query: #for searching on wikipedia
            speak('searching on wikipedia...')
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'search' in query: #to search on google
            searchgoogle()

        elif 'youtube' in query: #playing youtube video
            speak("what should i search for on youtube?")
            topic=takecommandMic()
            pywhatkit.playonyt(topic)

        elif 'news' in query:
            news()

        elif 'read' in query:
            texttospeech()

        elif 'covid' in query:
            covid()

        elif 'vs code' in query:
            speak("opening vs code")
            codepath='C:\\Users\\RAVI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)
        
        elif 'open' in query:
            speak("opening my documents")
            os.system('explorer C://{}'.format(query.replace('open','')))
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            speak("what should i remember?")
            data=takecommandMic()
            speak("you told me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you told me to remember that" +remember.read())

        elif 'password' in query:
            passwordgen()

        elif 'flip' in query:
            flip()

        elif 'offline' in query: #if we say offlime the jarvis will quit
            speak("going offline")
            quit()










#while (True):
    #voice=int(input("press 1 for male voice\n press 2 for female voice\n"))
    #audio=input("enter the text to convert to speech\n") #taking input from user

    #getvoices(voice,audio)
#while(True):   #taking multiple input from user
     #audio=input("enter the text to convert to speech\n") #taking input from user
     #speak(audio) #calling speak function