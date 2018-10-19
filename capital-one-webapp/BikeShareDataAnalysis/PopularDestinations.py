'''
Created on Oct 12, 2018

@author: markkang
'''
import pandas as pd 
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

def find_popular_stations():
    popularStartStation = reviews["Starting Station ID"].mode()
    popularEndingStation = reviews["Ending Station ID"].mode()
    return [popularStartStation, popularEndingStation]
    


if __name__ == '__main__':
    print (find_popular_stations())