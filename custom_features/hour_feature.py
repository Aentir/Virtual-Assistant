from contextlib import nullcontext
from datetime import datetime
from voice_config.talk_feature import talk

def get_hour(rec = nullcontext):
    hour = datetime.now().strftime('%I:%M %p')
    talk("Son las " + hour)