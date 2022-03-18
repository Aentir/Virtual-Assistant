from flask import request
import speech_recognition as sr #Importo paquete de reconocimiento de voz
import pyttsx3                  #Importo paquete para reproducir por audio
import pywhatkit
from datetime import datetime, date, timedelta
import AVMSpeechMath as sm
import requests
from translate import Translator

#Se inician los paquetes speech_recognition y pyttsx3
listener = sr.Recognizer() #Se instancia la clase speech_recognition con su funcionalidad "Recognizer"
engine = pyttsx3.init()    #Inicializo el modulo
name = 'alexa'
toggle = 1

#city = "Valencia"


# print(temp)
# print(wind)
# print(description)

day_es = [line.rstrip('\n') for line in open('src/day/day_es.txt')]
day_en = [line.rstrip('\n') for line in open('src/day/day_en.txt')]

# Otorga voz a nuestro asistente virtual
def talk(text):
    engine.say(text)
    engine.runAndWait()

rate = engine.getProperty('rate')   #Cambio la velocidad a la que habla
engine.setProperty('rate', 150)     #Establezco la velocidad

voices = engine.getProperty('voices')   #Elijo la voz que voy a usar
engine.setProperty('voice', voices[0].id)   #Establezco la voz que voy a usar



# Guardamos la entrada por voz y la redirigimos a otras funciones si conoce la petición, sino, nos devuelve mensaje de "error"
def listen():
    
    toggle = 1
    with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            rec = ""
    try:
        
            #El parametro "language" ayuda al reconocimiento de la voz, forzando a que sea en español en este caso
            rec = listener.recognize_google(voice, language='es-ES').lower()
            #Se eliminan los acentos de cualquier vocal
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            #rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                toggle = run(rec)
                print(rec)
            else:
                talk("Vuelve a intentarlo, no conozco: " + rec)         
    except:
        pass
        #print('Ha ocurrido un error!')
    return toggle

def iterateDays(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)

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
    elif 'dia' in rec:
        talk(f"Hoy es {getDay()}")
        #         if 'fue' in rec:
        #             talk(f"{getDaysAgo(rec)}")
        #         else:
        #             talk(f"Hoy es {getDay()}")
        
    elif 'cuanto es' in rec:
        #print(rec)
        talk(sm.getResult(rec))
        
    elif 'tiempo en' in rec:
        city = rec.replace('tiempo en', '')
        # print(city)
        # print(rec)
        # # "&units=metric" realiza la conversión de medida American a Europea
        # url_weather = "http://api.openweathermap.org/data/2.5/weather?q={}&lang=es&APPID=f2b990c09e6f73102863cfe63a569f43&units=metric".format(city)
        # #url_weather = "https://api.openweathermap.org/data/2.5/weather?q={},esp&units=metric&lang=es&APPID=f2b990c09e6f73102863cfe63a569f43".format(city)
        # talk("ok1")
        # print(url_weather)
        # res = requests.get(url_weather)
        # talk("ok2")
        # data = res.json()
        # temp = data["main"]["temp"]
        # wind = data["wind"]["speed"]
        # description = data["weather"][0]["description"]
        # talk("ok3")
        # print(temp)
        # print(wind)
        # print(description)
        # talk(str(float(temp)))
        # talk("En " + city + "hace " + temp + " grados")
        # talk("ok4")
        
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=f2b990c09e6f73102863cfe63a569f43&units=metric".format(city) #.format importante
            
            
        res = requests.get(url)

        data = res.json()
        print(data)
        temp = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]

        # latitude = data["coord"]["lat"]
        # longitude = data["coord"]["lon"]

        description = data["weather"][0]["description"]
        translate = Translator(to_lang="Spanish")
        translation = translate.translate(description)
        print(temp)
        talk("La temperatura es: " + str(float(temp)))               
        talk("La velocidad del viento es:" + str(wind_speed))
        # talk("La latitud es: " + str(latitude))
        # talk("La longitud es: " + str(longitude))
        talk("Hace un día " + translation)
            
    elif 'apagate' in rec:
        toggle = 0
        talk("Hasta luego")
    else:
        talk("Vuelve a intentarlo, no conozco: " + rec)
    return toggle
        
while toggle:      
    toggle = listen()
    
