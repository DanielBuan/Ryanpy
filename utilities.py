from datetime import datetime

def parse_full_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')

def parse_full_date_without_milisec(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')