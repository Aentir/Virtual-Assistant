import pywhatkit
from voice_config.talk_feature import talk
from formatter_voice_input.formatter_rec import formatter

def reproduce(rec):
    music = formatter(rec)
    talk('Reproduciendo ' + music)
    pywhatkit.playonyt(music)