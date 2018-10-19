'''
Created on Oct 17, 2018

@author: markkang
'''
import pandas as pd
import plotly.graph_objs as go
import plotly.offline 
import RegularCommuters
reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

def pass_holder_type_duration(reviews):
    durationOfPassType = {}
    
    for time, passType in zip(reviews["Duration"], reviews["Passholder Type"]):
        if passType not in durationOfPassType:
            durationOfPassType[passType] = 0
        durationOfPassType[passType] += int(time)
    return durationOfPassType
    

def find_average_duration(dic):
    for key, value in dic.items():
        totalPassType = RegularCommuters.common_passholder_type()[key]
        average = value / totalPassType
        dic[key] = average
    return dic
def visualize_total(dic):
    x1 = []
    y1 = []
    
    for key, value in dic.items():
        x1.append(key)
        y1.append(value/3600)
    trace1 = go.Bar(
                    x = x1,
                    y = y1,
                    marker=dict(
                        color='rgb(158,202,225)',
                    line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
                    )
    layout = dict(title = 'Total Hours used by Each Passholder Type',
              xaxis= dict(title= 'Passholder Type'),
              yaxis= dict(title = 'Total Hours Used'),
            
            )
    data=[trace1]
    fig = dict(data = data, layout = layout)
    plotly.offline.plot(fig)
def visualize_average(dic):
    x1 = []
    y1 = []
    
    for key, value in dic.items():
        x1.append(key)
        y1.append(value/60)
    trace1 = go.Bar(
                    x = x1,
                    y = y1,
                    marker=dict(
                        color='rgb(158,202,225)',
                    line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
                    )
    layout = dict(title = 'Average Minutes per Use by Each Passholder Type',
              xaxis= dict(title= 'Passholder Type'),
              yaxis= dict(title = 'Average Minutes each Use'),
            
            )
    data=[trace1]
    fig = dict(data = data, layout = layout)
    plotly.offline.plot(fig)
if __name__ == '__main__':
    visualize_average(find_average_duration(pass_holder_type_duration(reviews)))
    visualize_total(pass_holder_type_duration(reviews))