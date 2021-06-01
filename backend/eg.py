import datetime
import pytz

def giveMeTimeZome():
    value=[]
    n=0
    for tz in pytz.all_timezones:
        cple= (n, tz)
        value.append(cple)
        n+=1
    return value
i= giveMeTimeZome()
print(i)