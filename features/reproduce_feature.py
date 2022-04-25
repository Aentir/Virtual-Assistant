import pywhatkit
from features.talk_feature import talk


def reproduce(rec):
    music = rec.replace('reproduce', '')
    talk('Reproduciendo ' + music)
    pywhatkit.playonyt(music)