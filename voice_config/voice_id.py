#Paquete para dotar de habla a la aplicación
import pyttsx3 

def voice_id():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')   #Voz a usar
    engine.setProperty('voice', voices[0].id)   #Establece usar