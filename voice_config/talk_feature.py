#Paquete para dotar de habla a la aplicación
import pyttsx3

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()