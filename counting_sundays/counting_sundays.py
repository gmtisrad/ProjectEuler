days_in = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

days_of_week = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

def count_sundays(start_day, start_month, start_year, end_day, end_month, end_year):
    isLeapYear = False
    start_count = False

    year = 1900
    month = 0
    day = 0

    sunday_accumulator = 0

    current_dow = days_of_week[day]
    current_month = months[month]

    while year <= end_year or month <= end_month or day <= end_day:
        if (year == start_year) and (month == end_month) and (day == end_day):
            start_count = True
        if start_count:
            if current_dow == days_of_week[6] and check_first_of_month():
                sunday_accumulator += 1

def check_first_of_month(day, month, year):
    accumulator = 0

    if check_leap_year(year) and month >= 1:
        accumulator += 1

    for i in range(month):
        accumulator += days_in[i]

    if 0 == day % accumulator:
        print("first day")
        return True
    else:
        return False

def check_leap_year(year):
    if 0 == year % 4 and 0 != year % 400:
        # Add one to the accumulator due to leap year
        return True
    else:
        return False