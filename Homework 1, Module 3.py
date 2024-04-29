from datetime import datetime

def get_days_from_today(date):
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d")
        date_now = datetime.today()
        delta = date_now - new_date
        return delta.days
    except ValueError:
        return ("Enter valid date format - YYYY-MM-DD")
    
new_date = ("1999-11-10")
print (get_days_from_today(new_date))