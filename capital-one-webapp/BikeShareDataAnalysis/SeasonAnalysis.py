'''
Created on Oct 18, 2018

@author: markkang
'''

import pandas as pd
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

def trial(reviews):
    x=0
    for _ in reviews["Start Time"]:
        x+=1
    print(x)


def season_check(date):
    if  6<= int(date[5:7]) <= 8:
        return "Summer"
    elif 9<= int(date[5:7]) <= 11:
        return "Fall"
    elif int(date[5:7]) == 12 or (int(date[5:7]) == 1 or int(date[5:7]) ==2):
        return "Winter"
    elif 3 <= int(date[5:7]) <= 5:
        return "Spring"

def find_season_count(reviews):
    seasonCount = {}
    
    for date in reviews["Start Time"]: 
        season = season_check(date)
        if season not in seasonCount:
            seasonCount[season] = 0
        seasonCount[season] += 1
        
    return (seasonCount)

def find_season_duration(reviews):
    averageDurationEachSeason = {}
    for date, duration in zip(reviews["Start Time"], reviews["Duration"]): 
        season = season_check(date)
        if season not in  averageDurationEachSeason:
            averageDurationEachSeason[season] = 0
        averageDurationEachSeason[season] += int(duration)
    
    for season, duration in averageDurationEachSeason.items():
        totalDuration = averageDurationEachSeason[season] 
        totalCount = find_season_count(reviews)[season]
        averageDurationEachSeason[season] = totalDuration / totalCount
    print(averageDurationEachSeason)

if __name__ == '__main__':
    find_season_duration(reviews)