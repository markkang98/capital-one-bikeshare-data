'''
Created on Oct 18, 2018

@author: markkang
'''

import pandas as pd
import plotly.offline 
import plotly.graph_objs as go
from matplotlib.pyplot import title

reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

def trial(reviews):
    x=0
    for _ in reviews["Start Time"]:
        x+=1
    print(x)


def season_check(date):
    if  6<= int(date[5:7]) <= 8:
        return "summer"
    elif 9<= int(date[5:7]) <= 11:
        return "fall"
    elif int(date[5:7]) == 12 or (int(date[5:7]) == 1 or int(date[5:7]) ==2):
        return "winter"
    elif 3 <= int(date[5:7]) <= 5:
        return "spring"

def find_season_count(reviews):
    seasonCount = {}
    
    for date in reviews["Start Time"]: 
        season = season_check(date)
        if season not in seasonCount:
            seasonCount[season] = 0
        seasonCount[season] += 1
        
    return (seasonCount)

def find_season_duration(reviews):
    averageDurationEachSeason = {}
    for date, duration in zip(reviews["Start Time"], reviews["Duration"]): 
        season = season_check(date)
        if season not in  averageDurationEachSeason:
            averageDurationEachSeason[season] = 0
        averageDurationEachSeason[season] += int(duration)
    
    for season, duration in averageDurationEachSeason.items():
        totalDuration = averageDurationEachSeason[season] 
        totalCount = find_season_count(reviews)[season]
        averageDurationEachSeason[season] = totalDuration / (totalCount * 60)
    return (averageDurationEachSeason)

def find_season_pass_type(reviews):
    commonPassPerSeason = {}
    for date, passHolderType in zip(reviews["Start Time"], reviews["Passholder Type"]):
        season = season_check(date)
        if season not in commonPassPerSeason:
            commonPassPerSeason[season] = {}
        if passHolderType not in commonPassPerSeason[season]:
            commonPassPerSeason[season][passHolderType] = 0
        commonPassPerSeason[season][passHolderType] += 1
    print(commonPassPerSeason)
    return (commonPassPerSeason)

def visualize_season_pass_type(dic):
    season = input('Enter the season -> winter, summer, spring, fall:')
    seasonMap = dic[season]
    labels = []
    values = []
    for key, value in seasonMap.items():
        labels.append(key)
        values.append(value)
        
   
    
    trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo= 'value + label' , 
               textfont=dict(size=20),
               marker=dict( 
                           line=dict(color='#000000', width=2)))
    data = [trace]
    layout = go.Layout(
        title = 'Percentage of Passholder Types used in ' + season
        )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)
def visualize_average_season_duration(dic):
    x1 = []
    y1 = []
    
    for key, value in dic.items():
        x1.append(key)
        y1.append(value)
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
    layout = dict(title = 'Average Minutes per Use Each Season',
              xaxis= dict(title= 'Season'),
              yaxis= dict(title = 'Average Minutes each Use'),
            
            )
    data=[trace1]
    fig = dict(data = data, layout = layout)
    plotly.offline.plot(fig)
if __name__ == '__main__':
    #visualize_season_pass_type(find_season_pass_type(reviews))
    visualize_average_season_duration((find_season_duration(reviews)))