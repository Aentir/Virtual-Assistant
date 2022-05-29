#Paquete de reconocimiento de voz
import speech_recognition as sr                 
from custom_features.select_database import get_all_notes, get_last_note
from custom_features.insert_database import insert_database
from custom_features.delete_database import delete_database_info
from custom_features.day_features import response_day
from custom_features.hour_feature import get_hour
from custom_features.calc_feature import get_calc
from custom_features.weather_feature import get_weather
from custom_features.reproduce_feature import reproduce
from custom_features.adios_feature import adios
from voice_config.voice_id import voice_id 
from voice_config.voice_rate import voice_rate
from formatter_voice_input.formatter_rec import formatter

listener = sr.Recognizer() #Se instancia la clase speech_recognition con su funcionalidad "Recognizer"

name = 'alexa'  #Nombre de nuestro asistente virtual, se puede establecer otro cualquiera
toggle = 1

voice_id()
voice_rate()

features = {
        'reproduce': reproduce,
        'hora': get_hour,
        'que dia es': response_day,
        'cuanto es': get_calc,
        'raiz de': get_calc,
        'tiempo en': get_weather,
        'dime notas': get_all_notes,
        'dime ultima nota': get_last_note,
        'borra notas': delete_database_info,
        'apunta': insert_database,
        'apagate': adios
}

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
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            if name in rec:
                formatter(rec)
                toggle = run(formatter(rec)) 
    except:
        pass
    return toggle


def run(rec):
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