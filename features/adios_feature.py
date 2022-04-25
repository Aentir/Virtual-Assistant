from contextlib import nullcontext
from features.talk_feature import talk

def adios(rec = nullcontext):
    talk("Hasta luego")