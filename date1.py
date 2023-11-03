from datetime import datetime, timedelta
import json
from createscrape import createAndScrape
import time

def get_date():
    with open('date.json', 'r') as f:
        date = json.load(f)
        return date
    
def save_date(date):
    with open('date.json', 'w') as f:
        json.dump(date, f)

def add_to_readme(data_pass):
    with open('README.md', 'a') as f:
        f.write(f'{data_pass}\n\n')

# Input string
runHowManyTimes = 1

for i in range(runHowManyTimes):
    date_str = get_date()

    # Convert the string to a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Subtract one day using timedelta
    one_day = timedelta(days=1)
    new_date_obj = date_obj - one_day

    # Format the result as a string
    new_date_str = new_date_obj.strftime("%Y-%m-%d")

    print(new_date_str)

    save_date(new_date_str)

    # createAndScrape('Web3 Yarb', '2023', '2023', new_date_str, isToday=False)
    createAndScrape('Web3 Daily News Feed', new_date_str, '2023', new_date_str)

    # small delay to avoid getting blocked
    time.sleep(5)
