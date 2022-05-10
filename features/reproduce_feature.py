import pywhatkit
from features.talk_feature import talk
import formatter_rec


def reproduce(rec):
    music = formatter_rec.formatter(rec)
    #music = rec.replace('reproduce', '')
    talk('Reproduciendo ' + music)
    pywhatkit.playonyt(music)