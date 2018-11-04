'''
Created on Oct 19, 2018

@author: markkang
'''
import pandas as pd
import plotly.offline 
import plotly.graph_objs as go
from matplotlib.pyplot import title

reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

"""
create a dictionary of dictionaries. The key would be the passholder type and
the value would be another dictionary with keys of the trip route category and values of
the count of that trip route category. This creates a data structure that allows us to visualize
passholder type - trip route category correlations. 
"""
def find_correlation(review):
    corr = {}
    for passType, route in zip(reviews["Passholder Type"], reviews["Trip Route Category"]): 
        if passType not in corr: 
            corr[passType] = {}      #makes the key the passholder type and assigns dictionary to its value
        if route not in corr[passType]:   
            corr[passType][route] = 0
        corr[passType][route] += 1   #counts how many of the passholder type and trip route category combinations happen
    return corr


def visualize_correlation(dic): #create a double bar graph that shows values of trip route categories for each passholder type
    names = []
    roundTrip = []
    oneWay = []
    for key, value in dic.items():
        names.append(key)
        roundTrip.append(value['Round Trip'])
        oneWay.append(value['One Way'])
        
    trace1 = go.Bar(
    x= names,
    y= roundTrip,
    name='Round Trip'
    )
    
    trace2 = go.Bar(
    x=names,
    y= oneWay,
    name='One Way'
    )
    
    data = [trace1, trace2]
    layout = go.Layout( barmode='group')

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)

if __name__ == '__main__':
    visualize_correlation((find_correlation(reviews)))