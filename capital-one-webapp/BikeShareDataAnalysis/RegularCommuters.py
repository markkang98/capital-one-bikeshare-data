'''
Created on Oct 14, 2018

@author: markkang
'''
import pandas as pd 
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})


"""
returns a dictionary that has the passholder type as keys
and the count of how many rides by the passholder type as values
checks to see how many rides were made by regular commuters, not walk up
"""
def common_passholder_type():
    countPassholderType = {}
    for category in reviews["Passholder Type"]: 
        if category not in countPassholderType:
            countPassholderType[category] = 0
        countPassholderType[category] += 1      #counts each occurrence      
    return countPassholderType
    

if __name__ == '__main__':
    print(common_passholder_type())