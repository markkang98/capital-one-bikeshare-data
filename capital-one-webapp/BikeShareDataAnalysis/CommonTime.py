'''
Created on Oct 15, 2018

@author: markkang
'''
import pandas as pd 
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

averageDuration = reviews["Duration"].mean()

print(averageDuration)
if __name__ == '__main__':
    pass