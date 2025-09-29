import calendar

def show_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    print("\n===== Calendar =====")
    print(calendar.month(year, month))

show_calendar()