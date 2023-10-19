import datetime
from datetime import date
from speak import speak

today = date.today()
formatted_date = today.strftime("%d %b %Y")

now = datetime.datetime.now()


def wish():

    if now.hour < 12:
        speak("Good morning mam ")



    elif now.hour < 16:
        speak("Good afternoon mam ")


    else:
        speak("Good evening mam ")


def greating():
    if now.hour < 12:
        speak("Good morning mam ")



    elif now.hour < 16:
        speak("Good afternoon mam ")


    else:
        speak("Good evening mam ")