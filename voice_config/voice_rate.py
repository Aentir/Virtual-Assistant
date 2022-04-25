import pyttsx3 

def voiceRate():
    engine = pyttsx3.init()
    engine.getProperty('rate')   #Cambio la velocidad a la que habla
    engine.setProperty('rate', 150)     #Establezco la velocidad