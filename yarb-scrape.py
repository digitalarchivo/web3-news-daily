# coding:utf-8
from my_custom_package import add_to_readme, todayDateFileName, strdate, createAndScrape

def job():
    createAndScrape('Web3 Daily News Feed', todayDateFileName, '2023', strdate, isToday=True)
    add_to_readme(todayDateFileName, strdate)

    # loop 5 times - 307
    # for i in range(1, 424):
    #     # minus one day
    #     runDate2 = (dateNow - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
    #     yearString = runDate2.split('-')[0]
    #     print(yearString)
    #     print(runDate2)
    #     filename2 = 'days/{date}.md'.format(date=runDate2)
    #     # createAndScrape('Web3 Daily News Feed', filename, '2023', runDate)
    #     createAndScrape('Web3 Daily News Feed', filename2, yearString, runDate2)
    #     add_to_readme(filename2, runDate2)

if __name__ == '__main__':
    job()