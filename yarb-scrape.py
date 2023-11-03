# coding:utf-8
from my_custom_package import add_to_readme, todayDateFileName, strdate, createAndScrape

def job():
    createAndScrape('Web3 Daily News Feed', todayDateFileName, '2023', strdate, isToday=True)
    add_to_readme(todayDateFileName, strdate)



if __name__ == '__main__':
    job()