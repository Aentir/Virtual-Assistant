from contextlib import nullcontext
from voice_config.talk_feature import talk

def adios(rec = nullcontext):
    talk("Hasta luego")