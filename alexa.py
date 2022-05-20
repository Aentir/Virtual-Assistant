import speech_recognition as sr #Importo paquete de reconocimiento de voz
#import pyttsx3                  #Importo paquete para reproducir por audio
from custom_features.select_database import select_database
from custom_features.insert_database import insert_database
from custom_features.day_features import response_day
from custom_features.hour_feature import get_hour
from custom_features.calc_feature import get_calc
from custom_features.weather_feature import get_weather
from custom_features.reproduce_feature import reproduce
from custom_features.adios_feature import adios
from voice_config.voice_id import voiceId 
from voice_config.voice_rate import voiceRate
from formatter_voice_input.formatter_rec import formatter


#Se inician los paquetes speech_recognition y pyttsx3
listener = sr.Recognizer() #Se instancia la clase speech_recognition con su funcionalidad "Recognizer"
name = 'alexa'
toggle = 1

voiceId()
voiceRate()

features = {
        'reproduce': reproduce,
        'hora': get_hour,
        'que dia': response_day,
        'cuanto es': get_calc,
        'tiempo en': get_weather,
        'dame': select_database,
        'apunta': insert_database,
        'apagate': adios
}

# Guardamos la entrada por voz y la redirigimos a otras funciones si conoce la petición, sino, nos devuelve mensaje de "error"
def listen():
    toggle = 1
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
        
            #El parametro "language" ayuda al reconocimiento de la voz, forzando a que sea en español en este caso
            rec = listener.recognize_google(voice, language='es-ES').lower()
            #Se eliminan los acentos de cualquier vocal
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ny", "ñ")
            #rec = rec.lower()
            if name in rec:
                formatter(rec)
                toggle = run(formatter(rec)) 
    except:
        pass
        #print('Ha ocurrido un error!')
    return toggle

# Esta función aloja todas las funcionalidades que puede desarrollar el asistente virtual
def run(rec):
    #rec = listen()
    if 'apagate' in rec:
        features['apagate'](rec)
        toggle = 0
    else:
        for feature in features:
            if feature in rec:
                print(features[feature])
                features[feature](rec)
    return toggle
        
while toggle:      
    toggle = listen()
    
