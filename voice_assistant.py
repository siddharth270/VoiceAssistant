import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print('listeninig...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bolt' in command:
                command = command.replace('bolt', '')
                print(command)

    except:
        pass

    return (command)


def run_bolt():

    com = take_command()
    print(com)
    if 'play' in com:
        song = com.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in com:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'what' or 'who' or 'when' in com:
        wiki_search = com.replace('who' or 'what' or 'when', '')
        info = wikipedia.summary(wiki_search, 1)
        print(info)
        talk(info)

    elif 'Hey good morning' in com:
        ti = datetime.datetime.now().strftime('%I:%M %p')
        talk('A very good morning sir.')
        talk('The current time is ' + ti)
        talk('Here is your favorite song to begin your day on a happy note. Have a lovely day!')
        pywhatkit.playonyt('Sitare by nikhil d souza')

    else:
        talk('Sorry I could not get that')


while True:

    run_bolt()




