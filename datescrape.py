import json
from datetime import datetime, timedelta

# load json file date.json

def get_date():
    with open('date.json', 'r') as f:
        date = json.load(f)
        return date
    
def save_date(date):
    with open('date.json', 'w') as f:
        json.dump(date, f)

print(get_date())

dateinfile = get_date()
# dateinfileMinusOneDay = dateinfile - datetime.timedelta(days=1)

date_obj = datetime.strptime(dateinfile, "%Y-%m-%d")

# Subtract one day using timedelta
one_day = datetime.timedelta(days=1)
new_date_obj = date_obj - one_day

# Format the result as a string
new_date_str = new_date_obj.strftime("%Y-%m-%d")

print(new_date_str)

# save_date('2018-01-02')
# print(dateinfileMinusOneDay.strftime('%Y-%m-%d'))