import datetime
import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("language",'hi-in')

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 130)     # setting up new voice rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("hello sir i am  your virtual assistance. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #or r.recognize_google(audio, language='hi-in')    #language='hi-in'
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #or r.recognize_google(audio, language='hi-in')    #language='hi-in'
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def makefolder():
    speak("Directory name plz!")
    fname = takeCommand()
    dirc = os.mkdir("F:/" + fname)

    speak("folder succesfully have createt!")
    print(dirc)

def removefolder():
    speak("Directory name plz!")
    fname = takeCommand()
    dirc = os.removedirs("F:/" + fname)

    speak("folder succesfully Remove")
    print(dirc)

def readfile():
    speak("file name plz!")
    n = 50
    fname = takeCommand()
    fd = os.open("F:/" + fname + ".txt", os.O_RDONLY)
    dirc = os.read(fd, n)

    speak(dirc)
    print(dirc)

def playmusic():
    music_dir = 'F:\\songs'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

def openvideo():
    music_dir = 'D:\\vikas collection\\Videos\\Web Series\\sherlock'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

def makefile():
    speak('directory name sir! ')
    fname = takeCommand()
    f = open(fname + ".txt", "a")
    print(fname)
    f.close()
    speak('file make succesfully sir!')


def writeinfile():
    speak('directory name sir! ')

    fname = takeCommand()
    f = open(fname + ".txt", "a")
    print(fname)
    speak('what do you want to write sir!')

    query = takeCommand()
    f.write(query + " ")
    print(query)
    speak('writing has been complited complited sir!')
    f.close()