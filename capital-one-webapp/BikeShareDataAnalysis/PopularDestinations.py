'''
Created on Oct 12, 2018

@author: markkang
'''
import pandas as pd 
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

"""
returns a list of two items. first is the most 
popular starting station and the second is the
most popular ending station
"""
def find_popular_stations():
    popularStartStation = reviews["Starting Station ID"].mode()
    popularEndingStation = reviews["Ending Station ID"].mode()
    return [popularStartStation, popularEndingStation]
    


if __name__ == '__main__':
    print (find_popular_stations())