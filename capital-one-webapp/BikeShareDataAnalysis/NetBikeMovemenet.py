'''
Created on Oct 19, 2018

@author: markkang
'''
import pandas as pd
import math

reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

def net_movement(reviews, year, month, day):
    target = year + "-" + month + "-" + day
    stationNet = {}
    n = 0
    for startingID, endingID, date in zip(reviews["Starting Station ID"], reviews["Ending Station ID"], reviews["Start Time"]): 
        if(target == date[0:10]):
            if math.isnan(startingID) or math.isnan(endingID):
                n += 1
                continue
            if int(startingID) not in stationNet:
                stationNet[int(startingID)] = 0
            stationNet[int(startingID)] -= 1
            if int(endingID) not in stationNet:
                stationNet[int(endingID)] = 0
            stationNet[int(endingID)] += 1
    print(n)
    print(stationNet)

if __name__ == '__main__':
    net_movement(reviews, "2016","07", "09")