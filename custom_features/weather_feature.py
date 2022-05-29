import requests
from voice_config.talk_feature import talk
from formatter_voice_input.formatter_rec import formatter

def get_weather(rec):
    city = formatter(rec).split()
    city.pop(0)
    city = ' '.join(city)
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&lang=es&appid=f2b990c09e6f73102863cfe63a569f43&units=metric".format(city)
    print(url)
    res = requests.get(url)
    data = res.json()
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    print(temp)
    print(wind_speed)
    print(description)
        
    talk("La temperatura es: " + str(float(temp)) + " grados")               
    talk("La velocidad del viento es:" + str(wind_speed) + " kilometros hora")
    talk("Hace un día " + description)