from datetime import datetime
import calendar
current_datetime = datetime.now()
some_date = datetime(2021, 7, 14)
date_as_string = "Feb 14 2021 8:30AM"

if __name__ == '__main__':
    print(current_datetime.year)
    print(some_date.weekday())
    a = current_datetime.year
    if calendar.isleap(a):
        print(f'{a} is a leap year')
    else:
        print(f'{a} is not a leap year')
    datetime_object = datetime.strptime(date_as_string, "%b %d %Y %H:%M%p")
    print(datetime_object)
