'''
Created on Nov 3, 2018

@author: markkang
'''

import pandas as pd
import math
import plotly.offline 
import plotly.plotly as py 
import plotly.graph_objs as go

reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})


def find_coordinates(reviews):
    stationID = []
    x = []
    y = []
    for startID, startLat, startLong, endID, endLat, endLong in zip(reviews["Starting Station ID"], reviews["Starting Station Latitude"], reviews["Starting Station Longitude"],reviews["Ending Station ID"],reviews["Ending Station Latitude"],reviews["Ending Station Longitude"]):
        if math.isnan(startID) or math.isnan(endID):
            continue
        if startID not in stationID:
            stationID.append(str(int(startID)))
            x.append(str(startLat))
            y.append(str(startLong))
        if endID not in stationID:
            stationID.append(str(int(endID)))
            x.append(str(endLat))
            y.append(str(endLong))
            
    return [x,y, stationID]


def visualize(reviews):
    x = []
    y = []
    for p in  find_coordinates(reviews)[0][0:10]:
        x.append(p)
    for p in  find_coordinates(reviews)[1][0:10]:
        y.append(p)
    print(x)
    print(y)
    z = find_coordinates(reviews)[2]
    mapbox_access_token = 'pk.eyJ1IjoibWFya2thbmc5OCIsImEiOiJjam8yNTRiaWowaW9wM3Fxc205a2J2c2lqIn0.nOJG5OtIk1-ljg9xXKkWGA'
    data = [
        go.Scattermapbox(
            lat = x,
            lon = y,
            mode='markers',
            marker=dict(
                size=9
                ),
            text= z
            )
    ]

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=38.92,
                lon=-77.07
                ),
            pitch=0,
            zoom=10
            ),
    )
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig)
    
if __name__ == '__main__':
    visualize(reviews)