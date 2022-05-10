import speech_recognition as sr #Importo paquete de reconocimiento de voz
#import pyttsx3                  #Importo paquete para reproducir por audio
from features.selectDatabase import selectDatabase
from features.insertDatabase import insertDatabase
from features.day_features import responseDay
from features.hour_feature import getHour
from features.calc_feature import getCalc
from features.weather_feature import getWeather
from features.reproduce_feature import reproduce
from features.adios_feature import adios
from voice_config.voice_id import voiceId 
from voice_config.voice_rate import voiceRate
from features_list.features_list import features_list
from formatter_voice_input.formatter_rec import formatter

#Se inician los paquetes speech_recognition y pyttsx3
listener = sr.Recognizer() #Se instancia la clase speech_recognition con su funcionalidad "Recognizer"
#engine = pyttsx3.init()    #Inicializo el modulo
name = 'alexa'
toggle = 1

# Otorga voz a nuestro asistente virtual
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

voiceId()
voiceRate()

features = {
        'reproduce': reproduce,
        'hora': getHour,
        'que dia': responseDay,
        'cuanto es': getCalc,
        'tiempo en': getWeather,
        'dame': selectDatabase,
        'apunta': insertDatabase,
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
            #rec = ""
        
            #El parametro "language" ayuda al reconocimiento de la voz, forzando a que sea en español en este caso
            rec = listener.recognize_google(voice, language='es-ES').lower()
            #Se eliminan los acentos de cualquier vocal
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ny", "ñ")
            #rec = rec.lower()
            if name in rec:
                formatter(rec)
                #print(rec.split())
                # array_name = rec.split()
                # array_name.pop(0)
                # #print(' '.join(array_name))
                # #print(rec)
                # rec = ' '.join(array_name)
                toggle = run(formatter(rec))
                #print(rec)
            # else:
            #     print(rec)
            #     talk("Vuelve a intentarlo, no conozco: " + rec)
            #     #listen()   
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
        
    # elif 'dame' in rec:
    #     print(rec)
    #     try:
    #         if 'receta macarrones' in rec:
    #             keyword = 'macarrones'
    #             talk(database_methods.selectDatabase(keyword))
    #     except:
    #             talk("No he encontrado nada")
    
    # elif 'apunta' in rec:
    #     info = rec.split()
    #     keyword = info[-1]
    #     info.pop(0)
    #     formattedKeyWord =' '.join(info)
    #     print(keyword)
    #     print(formattedKeyWord)
    #     #keyword = rec.replace('apunta', "")
    #     #database_methods.setKeyWordDatabase(keyword)
    #     # print(rec)
    #     # print(keyword)
        
    #     description = rec.split()
    #     # description.pop(0, 1, 2, 3)
        
    #     # descript = rec.replace('apunta', "")
    #     print(description)
    #     #database_methods.updateDatabase(descript)
        
    # # elif 'guarda' in rec:
    # #     description = rec.split()
    # #     description.pop(0)
    # #     #va borrando indices del array, cuidado
    # #     description.pop(1)
    # #     description.pop(2)
    # #     description.pop(3)
    # #     print(description)
        
    # elif 'limpia base de datos' in rec:
    #      database_methods.deleteDatabaseInfo()
            
    # elif 'apagate' in rec:
    #     toggle = 0
    #     talk("Hasta luego")
    # else:
    #     talk("Vuelve a intentarlo, no conozco: " + rec)
    return toggle
        
while toggle:      
    toggle = listen()
    
