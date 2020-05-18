import datetime
from dateutil.parser import parse

def now():
    return datetime.datetime.now()

def now_iso():
    return now().isoformat()

def now_timestamp():
    return datetime.datetime.now().timestamp()

def calculate_difference_in_days(current_date, future_date):
    return (future_date - current_date).days