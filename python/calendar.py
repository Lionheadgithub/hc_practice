import sys
import datetime

def get_date_info():
    today = datetime.date.today()
    this_year = today.year
    this_month = today.month
    return this_year, this_month


def option(this_year, this_month):
    if "-m" in sys.argv:
        try:
            this_month = int(sys.argv[2])
            if not (1 <= this_month <= 12):
                print(f"{this_month} is neither a month number (1..12) nor a name")
                exit()
        except ValueError:
            print(f"{str(sys.argv[2])} is neither a month number (1..12) nor a name")
            exit()
    return this_year, this_month


def create_calendar(this_year, this_month):
    year_month = f"{this_month}月 {this_year}"
    print(year_month.center(21))
    weekdays = "月", "火", "水", "木", "金", "土", "日"
    for weekday in weekdays:
        print(f"{weekday:>2}", end="")
    print()

    if this_month == 12:
        next_month_first_day = datetime.date(this_year + 1, 1, 1)
    else:
        next_month_first_day = datetime.date(this_year, this_month + 1, 1)

    last_day = next_month_first_day - datetime.timedelta(days=1)
    first_day_number = datetime.date(this_year, this_month, 1).weekday()

    for _ in range(first_day_number):
        print(f"{" ":>2}", end=" ")
    for day in range(1, last_day.day + 1):
        print(f"{day:>2}", end=" ")
        if (day + first_day_number) % 7 == 0:
            print()
        else:
            continue
    print()
    
this_year, this_month  = get_date_info()
this_year, this_month = option(this_year, this_month)
create_calendar(this_year, this_month)