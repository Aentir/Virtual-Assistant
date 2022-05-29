#Paquete para dotar de habla a la aplicación
import pyttsx3 

def voice_rate():
    engine = pyttsx3.init()
    engine.getProperty('rate')   #Cambio velocidad habla
    engine.setProperty('rate', 150)     #Establece velocidad