'''
Created on Oct 16, 2018

@author: markkang
'''
import pandas as pd
import plotly.graph_objs as go
import plotly.offline 

reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})


def find_common_times(reviews):
    commonTimes = {}
    
    
    for date in reviews["Start Time"]: 
        if int(date[11:13]) not in commonTimes:
            commonTimes[int(date[11:13])] = 0
        commonTimes[int(date[11:13])] += 1
        
    return dict(sorted(commonTimes.items()))

def find_common_dates(reviews):
    commonDates = {}
    for date in reviews["Start Time"]: 
        if date[0:10] not in commonDates:
            commonDates[date[0:10]] = 0
        commonDates[date[0:10]] += 1
        
    return dict(sorted(commonDates.items()))
def visualize_hourly_use(dic):
    x1 = []
    y1 = []
    
    for key, value in dic.items():
        x1.append(key)
        y1.append(value/ len(dic))
    trace1 = go.Scatter(
                    x = x1,
                    y = y1,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    )
    layout = dict(title = 'BikeShares for each hour of the day',
              xaxis= dict(title= 'Hour of the Day', ticklen= 5,zeroline= False),
              yaxis= dict(title = 'Average number of Bikes Used'),
            
            )
    data=[trace1]
    fig = dict(data = data, layout = layout)
    plotly.offline.plot(fig)
    
    
def visualize_daily_use(dic):
    x1 = []
    y1 = []
    
    for key, value in dic.items():
        x1.append(key)
        y1.append(value)
    trace1 = go.Scatter(
                    x = x1,
                    y = y1,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    )
    layout = dict(title = 'Growth of BikeShares',
              xaxis= dict(title= 'Day', ticklen= 5,zeroline= False),
              yaxis= dict(title = 'Total number of bikes used'),
            
            )
    data=[trace1]
    fig = dict(data = data, layout = layout)
    plotly.offline.plot(fig)
if __name__ == '__main__':
    visualize_daily_use(find_common_dates(reviews))
    
    