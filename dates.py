import datetime

def get_dates(from_date, to_date, day_list=[0,1,2,3,4,5,6]):
    date_list = list()
    temp_list = list()
    ## Creates a list of all the dates falling between the from_date and to_date range
    for x in iter(range((to_date - from_date).days + 1)):
        temp_list.append(from_date + datetime.timedelta(days=x))
    for date_record in temp_list:
        if date_record.weekday() in day_list:
            date_list.append(date_record)
    return date_list


from_date = datetime.datetime(2019, 4, 23)
to_date = datetime.datetime(2019, 4, 28)

listDates = get_dates(from_date, to_date)
print(listDates)
