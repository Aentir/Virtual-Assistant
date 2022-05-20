from contextlib import nullcontext
from datetime import date
from custom_features.talk_feature import talk

day_es = [line.rstrip('\n') for line in open('day/day_es.txt')]
day_en = [line.rstrip('\n') for line in open('day/day_en.txt')]

def iterate_days(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def get_day():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterate_days(now)

def response_day(rec = nullcontext):
    talk(f"Hoy es {get_day()}")