'''
Created on Oct 14, 2018

@author: markkang
'''
import pandas as pd 
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

def common_passholder_type():
    countPassholderType = {}
    for category in reviews["Passholder Type"]: 
        if category not in countPassholderType:
            countPassholderType[category] = 0
        countPassholderType[category] += 1            
    return countPassholderType
    

if __name__ == '__main__':
    print(common_passholder_type())