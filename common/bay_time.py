import datetime
from pytz import timezone
import time


import locale

locale.setlocale(locale.LC_ALL,'id_ID.UTF-8')

def now():
    return to_local_datetime(now_millis())


def now_millis():
    milliseconds = int(round(time.time() * 1000))
    return milliseconds

def to_local_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000,timezone('Asia/Jakarta'))

def to_local_datetime_string(millis):
    return datetime.datetime.fromtimestamp(millis/1000,timezone('Asia/Jakarta')).strftime("%d %B %Y %H:%M")


def get_day_date_time(date):
    return date.strftime("%d %B %Y %H:%M")