from contextlib import nullcontext
from custom_features.talk_feature import talk

def adios(rec = nullcontext):
    talk("Hasta luego")