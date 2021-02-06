import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit
import datetime
import wikipedia
import os
listen= sr.Recognizer()
def audio(text):
    engine=pt.init()
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Please speak')
            audio("Please say a command")
            voice=listen.listen(source)
            command=listen.recognize_google(voice)
            command=command.lower()
            if 'cat' in command:
                command=command.replace('cat','')
                print(command)
    except:
        pass
    return command

def run():
    
    command= take_command()
    if 'play' in command:
        song=command.replace('play','')
        audio('Yes sir, playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        audio('Its '+ time)
    elif 'tell me about' in command:
        obj=command.replace('tell me about','')
        info=wikipedia.summary(obj, 1)
        audio(info)
    elif 'cook' in command:
        audio('Heres a video for the recipe')
        pywhatkit.playonyt(command)
    elif 'open chrome' in command:
        app=command.replace('open','')
        audio('opening '+app)
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome")
    elif 'open notepad' in command:
        audio('Opening notepad')
        os.system('Notepad')
    elif 'add' in command:
        exc=command.replace('add','')
        exc=exc.replace('and','/')
        num1=int(exc.split('/')[0])
        print(num1)
        num2=int(exc.split('/')[1])
        sum=num1+num2
        print(sum)
        sum=str(sum)
        audio('The sum is'+sum)
    elif 'subtract' in command:
        exc=command.replace('subtract','')
        exc=exc.replace('from','/')
        num1=int(exc.split('/')[0])
        print(num1)
        num2=int(exc.split('/')[1])
        diff=num2-num1
        print(diff)
        diff=str(diff)
        audio('The difference is'+diff)
    
    elif 'multiply' in command:
        exc=command.replace('multiply','')
        exc=exc.replace('and','/')
        num1=int(exc.split('/')[0])
        num2=int(exc.split('/')[1])
        prod=num1*num2
        print(prod)
        prod=str(prod)
        audio('The product is'+prod)
    elif 'divide' in command:
        exc=command.replace('divide','')
        exc=exc.replace('from','/')
        num1=int(exc.split('/')[0])
        print(num1)
        num2=int(exc.split('/')[1])
        diff=num1/num2
        print(diff)
        diff=str(diff)
        audio('The quiotient is'+diff)
    elif 'sleep' in command:
        audio.sleep()
    else:
        audio('Please repeat yourself u werent clear')
     
while True:
    run()