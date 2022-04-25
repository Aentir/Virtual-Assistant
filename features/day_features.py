from datetime import date

day_es = [line.rstrip('\n') for line in open('day/day_es.txt')]
day_en = [line.rstrip('\n') for line in open('day/day_en.txt')]


def iterateDays(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)