import pyttsx3 

def voiceId():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')   #Elijo la voz que voy a usar
    engine.setProperty('voice', voices[0].id)   #Establezco la voz que voy a usar