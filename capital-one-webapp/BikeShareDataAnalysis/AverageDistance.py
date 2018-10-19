'''
Created on Oct 13, 2018

@author: markkang
'''

import math
import pandas as pd
review = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

reviews = pd.DataFrame(review)
def find_series_distance(reviews):
    latitude1 = math.radians(reviews["Starting Station Latitude"])
    latitude2 = math.radians(reviews["Ending Station Latitude"])
    longitude1 = math.radians(reviews["Starting Station Longitude"])
    longitude2 = math.radians(reviews["Ending Station Longitude"])
    
    earthRadius = 6373.0
    
    diffLat = latitude1 - latitude2
    diffLon = longitude1 - longitude2
    
    temp = math.sin(diffLat / 2) **2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(diffLon /2) ** 2
    x = 2 * math.asin(math.sqrt(temp))
    
    distance = earthRadius * x
    
    return distance 

def find_average_distance():
    return reviews.apply(find_series_distance, axis =1).mean()
        
if __name__ == '__main__':
    print(find_average_distance())