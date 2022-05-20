from contextlib import nullcontext
from custom_features.talk_feature import talk
import AVMSpeechMath as sm

def get_calc(rec):
    talk(sm.getResult(rec))