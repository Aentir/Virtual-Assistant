import requests
from translate import Translator
from features.talk_feature import talk

def getWeather(rec):
    city = rec.replace('tiempo en', '')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=f2b990c09e6f73102863cfe63a569f43&units=metric".format(city) #.format importante
    res = requests.get(url)
    data = res.json()
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
        
    translate = Translator(to_lang="Spanish")
    translation = translate.translate(description)
    talk("La temperatura es: " + str(float(temp)) + " grados")               
    talk("La velocidad del viento es:" + str(wind_speed) + " kilometros hora")
    talk("Hace un día " + translation)