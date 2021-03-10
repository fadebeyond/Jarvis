import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from ShazamAPI import Shazam

listener = sr.Recognizer()
engine = pyttsx3.init()
newVoiceRate = 125
engine.setProperty('rate',newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=2)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now()
        day=str(date.day)
        month=str(date.month)
        year=str(date.year)

        talk('Todays date is ' + day )
        talk(month)
        talk(year)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hello sir')
    elif 'how are you today' in command:
        talk('I am good sir')
    elif 'which song is this' in command:
        mp3_file_content_to_recognize = open('a.mp3', 'rb').read()

        shazam = Shazam(mp3_file_content_to_recognize)
        recognize_generator = shazam.recognizeSong()
        while True:
	        talk(next(recognize_generator))
    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
