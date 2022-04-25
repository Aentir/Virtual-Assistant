from contextlib import nullcontext
from datetime import datetime
from features.talk_feature import talk

def getHour(rec = nullcontext):
    hour = datetime.now().strftime('%I:%M %p')
    talk("Son las " + hour)