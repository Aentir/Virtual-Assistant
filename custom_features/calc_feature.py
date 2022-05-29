from contextlib import nullcontext
from voice_config.talk_feature import talk
import AVMSpeechMath as sm

def get_calc(rec):
    talk(sm.getResult(rec))