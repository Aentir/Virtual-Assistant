import speech_recognition as sr #Importo paquete de reconocimiento de voz
import pyttsx3                  #Importo paquete para reproducir por audio
import pywhatkit
from datetime import datetime
import AVMSpeechMath as sm
import requests
from translate import Translator
import database_methods
from features.day_features import getDay
from voice_config.voice_id import voiceId 
from voice_config.voice_rate import voiceRate

#Se inician los paquetes speech_recognition y pyttsx3
listener = sr.Recognizer() #Se instancia la clase speech_recognition con su funcionalidad "Recognizer"
engine = pyttsx3.init()    #Inicializo el modulo
name = 'alexa'
toggle = 1

# Otorga voz a nuestro asistente virtual
def talk(text):
    engine.say(text)
    engine.runAndWait()

voiceId()
voiceRate()

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
                #print(rec.split())
                array_name = rec.split()
                array_name.pop(0)
                #print(' '.join(array_name))
                #print(rec)
                rec = ' '.join(array_name)
                toggle = run(rec)
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
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    #elif 'que' in rec:
    elif 'hora' in rec:
        hour = datetime.now().strftime('%I:%M %p')
        talk("Son las " + hour)
    elif 'que dia' in rec:
        talk(f"Hoy es {getDay()}")
    elif 'cuanto es' in rec:
        talk(sm.getResult(rec))
        
    elif 'tiempo en' in rec:
        city = rec.replace('tiempo en', '')
        # # "&units=metric" realiza la conversión de medida American a Europea
        # url_weather = "http://api.openweathermap.org/data/2.5/weather?q={}&lang=es&APPID=f2b990c09e6f73102863cfe63a569f43&units=metric".format(city)
        # #url_weather = "https://api.openweathermap.org/data/2.5/weather?q={},esp&units=metric&lang=es&APPID=f2b990c09e6f73102863cfe63a569f43".format(city)
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=f2b990c09e6f73102863cfe63a569f43&units=metric".format(city) #.format importante
            
            
        res = requests.get(url)

        data = res.json()
        print(data)
        temp = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        
        translate = Translator(to_lang="Spanish")
        translation = translate.translate(description)
        print(temp)
        talk("La temperatura es: " + str(float(temp)) + " grados")               
        talk("La velocidad del viento es:" + str(wind_speed) + " kilometros hora")
        talk("Hace un día " + translation)
    
    elif 'dame' in rec:
        print(rec)
        try:
            if 'receta macarrones' in rec:
                keyword = 'macarrones'
                talk(database_methods.selectDatabase(keyword))
        except:
                talk("No he encontrado nada")
    
    elif 'apunta' in rec:
        info = rec.split()
        keyword = info[-1]
        info.pop(0)
        formattedKeyWord =' '.join(info)
        print(keyword)
        print(formattedKeyWord)
        #keyword = rec.replace('apunta', "")
        #database_methods.setKeyWordDatabase(keyword)
        # print(rec)
        # print(keyword)
        
        description = rec.split()
        # description.pop(0, 1, 2, 3)
        
        # descript = rec.replace('apunta', "")
        print(description)
        #database_methods.updateDatabase(descript)
        
    # elif 'guarda' in rec:
    #     description = rec.split()
    #     description.pop(0)
    #     #va borrando indices del array, cuidado
    #     description.pop(1)
    #     description.pop(2)
    #     description.pop(3)
    #     print(description)
        
    elif 'limpia base de datos' in rec:
         database_methods.deleteDatabaseInfo()
            
    elif 'apagate' in rec:
        toggle = 0
        talk("Hasta luego")
    else:
        talk("Vuelve a intentarlo, no conozco: " + rec)
    return toggle
        
while toggle:      
    toggle = listen()
    
