'''
Created on Oct 19, 2018

@author: markkang
'''
import pandas as pd
import plotly.offline 
import plotly.graph_objs as go
from matplotlib.pyplot import title

reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})


def find_correlation(review):
    corr = {}
    for passType, route in zip(reviews["Passholder Type"], reviews["Trip Route Category"]): 
        if passType not in corr:
            corr[passType] = {}
        if route not in corr[passType]:
            corr[passType][route] = 0
        corr[passType][route] += 1
    print(corr)
    return corr

def visualize_correlation(dic):
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