'''
Created on Nov 4, 2018

@author: markkang
'''
import pandas as pd
import math
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dash.dependencies import Input, Output


reviews = pd.read_csv("metro-bike-share-trip-data.csv", dtype = {"Starting Lat-Long": str})

"""
net_movement creates a dictionary of dictionaries where we store dates as keys and the value is another dictionary that 
stores stationID as a key, and the net bike surplus or deficit in its values. We add 1 if a bike is added to that station, meaning it
is an ending station. We subtract 1 if a bike is taken from the station, meaning it is a starting station. 
"""

def net_movement(reviews):
    stationNet = {}
    n = 0
    for startingID, endingID, day in zip(reviews["Starting Station ID"], reviews["Ending Station ID"], reviews["Start Time"]):
        date = day[0:10] #splices the start time column to get the date 
        if math.isnan(startingID) or math.isnan(endingID): #checks for non existent values
            n += 1
            continue
        if(date not in stationNet):
            stationNet[date] = {}
        if int(startingID) not in stationNet[date]:
            stationNet[date][int(startingID)] = 0
        stationNet[date][int(startingID)] -= 1
        if int(endingID) not in stationNet[date]:
            stationNet[date][int(endingID)] = 0
        stationNet[date][int(endingID)] += 1
    return (stationNet)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server                                         #server will run- this python app will be deployed and shown in an iframe
app.layout = html.Div([
    dcc.Input(id='my-id', value='Enter the Date', type='text'),
    html.Div(id='p_section')
    
])


@app.callback(dash.dependencies.Output('p_section','children'), 
    [dash.dependencies.Input('my-id', 'value')]
)
def update_output_div(input_value):
    dic = net_movement(reviews)
    net = dic[input_value]
    
    identification = []
    netMovement = []
    for key, value in net.items(): #inputs the keys which are stationIDs and values which are net movement values in two separates lists
        identification.append(key)
        netMovement.append(value)
    trace = [go.Table(                                                      #create a plotly table to display the data
        header=dict(values=['Station ID', 'Surplus or Deficit of Bikes'],
                line = dict(color='#7D7F80'),
                fill = dict(color='#a1c3d1'),
                align = ['left'] * 5),
        cells=dict(values=[identification,
                       netMovement],
               line = dict(color='#7D7F80'),
               fill = dict(color='#EDFAFF'),
               align = ['left'] * 5))]
    
    
    fig = dcc.Graph(
        id='example',
        figure={
            'data': trace
        }
    )
    
    return fig


    
if __name__ == '__main__':
    app.run_server()