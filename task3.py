import datetime
import calendar
from functools import wraps

def format_date(func):
    """Decorator to format date as 'yyyy-mm/d'."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        date_obj = func(*args, **kwargs)
        return date_obj.strftime('%Y-%m/%d')
    return wrapper

@format_date
def first_day_of_last_week(input_date):
    """Calculates the first day of the last week in the month of the given date."""

    # Get the first day of the next month
    next_month = input_date.replace(day=28) + datetime.timedelta(days=4)  # Ensures we're in the next month
    first_of_next_month = next_month.replace(day=1)

    # Last day of the input_date's month is one day before the first of next month
    last_day_of_month = first_of_next_month - datetime.timedelta(days=1)

    # Get a calendar object for the current month
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    month_days = cal.itermonthdates(input_date.year, input_date.month)

    # Find the last week in the month
    last_week = []
    for day in month_days:
        if day.month == input_date.month:
            last_week.append(day)

    # Return the first day of the last week
    return last_week[0]


while True:
    try:
        # Get user input for the date
        date_str = input("Enter a date in YYYY-MM-DD format: ")
        input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()  # Parse input as date

        # Calculate the first day of the last week
        result_date = first_day_of_last_week(input_date)

        # Print the result
        print("First day of the last week:", result_date)
        break  # Exit the loop after successful calculation
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")