from datetime import datetime, timedelta

# calculate difference between 2 times
current_datetime = datetime(day=8, month=7, year=2021)
current_date = datetime(day=14, month=6, year=2022)

if __name__ == '__main__':
    value1 = current_datetime - timedelta(days=15)
    print(value1.strftime("%Y-%m-%d"))

    value2 = current_datetime + timedelta(days=7)
    print(value2.strftime("%Y-%m-%d"))

    value3 = current_date + timedelta(days=25)
    print(f'Hello Friedrich, your rent of 300 € is due on {value3.strftime("%Y-%m-%d")}')

