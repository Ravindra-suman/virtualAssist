import datetime
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning sir')
    elif hour >= 12 and hour < 16:
        speak('good afternoon sir')
    else:
        speak('good evening sir')

    speak('what can i do for you sir')


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listenting.....')
        audio = r.listen(source)
        r.pause_threshold = 1

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print('user said', query)

    except Exception as e:
        print('sorry! say that again.')
        return 'None'
    return query


if __name__ == '__main__':
    greetme()

    if 1:
        query = command().lower()

        if 'open notepad' in query:
            npath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories'
            os.startfile(npath)

        elif 'open cmd' in query:
            os.system('start cmd')

        elif 'play music' in query:
            mpath = 'E:\\Music\\'
            music = os.listdir(mpath)
            print(music)
            r=random.choice(music)
            for songs in music:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(mpath, songs))

        elif 'wikipedia' in query:
            print("searching wikipedia......")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            # print(f"the value of a is {a}")

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is {time}')

        elif "open google" in query:
            webbrowser.open('www.google.com')
        elif "open youtube" in query:
            webbrowser.open('www.youtube.com')

        elif "open instagram" in query:
            webbrowser.open('www.instagram.com')

        elif "open facebook" in query:
            webbrowser.open('www.facebook.com')

        elif "open whatsapp" in query:
            webbrowser.open('www.whatsapp.com')
            


        # elif "make folder" or " create folder" in query:
        #
        #     speak("folder name please!")
        #     fname =command()
        #     dirc = os.mkdir("F:/" + fname)
        #
        #     speak("folder succesfully created!")
        #     print(dirc)
        #
        # elif "delete folder" or "remove folder" in query:
        #     speak("folder name please")
        #     fname=command()
        #     dirc=os.removedirs("F:/"+fname)
        #     speak("folder succesfully deleted")

        elif "please switch window" in query:
            pass

        # elif 'send message' in query:
        #     pk.sendwhatmsg("+919664451320","hii priyanshu",10,23)
        #
        # elif "play" in query:
        #     pk.playonyt("2002")
