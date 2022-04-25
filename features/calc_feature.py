from contextlib import nullcontext
from features.talk_feature import talk
import AVMSpeechMath as sm

def getCalc(rec):
    talk(sm.getResult(rec))