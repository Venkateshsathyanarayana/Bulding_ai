import speech_recognition as sr            #install python speech recognition, install pyttsx3, install pyaudio,pip install pywhatkit
import pyttsx3                              #pip install wikipedia
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()                #for listening
engine = pyttsx3.init()                      #for ai to talk
#voices = engine.getProperty('voices)
#engine.setProperty('voice',voices[1].id)     #to convert the voice to male to female etc....            
def  talk(text):
    engine.say(text)                      # it speaks this
    engine.runAndWait()                           #waits for our speech 
   
def take_command():
    command=''
    try:
        with sr.Microphone() as source: 
            print('listening......')                    # to listen and type the line
            voice = listener.listen(source)             
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:               # if i say jarvis before any sentence it types 
             command = command.replace('jarvis','')
             print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing song' + song)
        pywhatkit.playonyt(song)                      #plays song on youtube
    elif 'time' in command:
        #time = datetime.datetime.now().strftime('%H:%M') 
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+ time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person)
        print(info)
        talk(info)
run_jarvis()