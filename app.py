#!/usr/bin/env python
# coding: utf-8



import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import base64


from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go


# ## Import datasets




circuits =pd.read_csv('f1db_csv/circuits.csv')

constructor_results = pd.read_csv('f1db_csv/constructor_results.csv')

constructor_standings = pd.read_csv('f1db_csv/constructor_standings.csv')

constructors =pd.read_csv('f1db_csv/constructors.csv')

driver_standings =pd.read_csv('f1db_csv/driver_standings.csv')

drivers =pd.read_csv('f1db_csv/drivers.csv')

lap_times =pd.read_csv('f1db_csv/lap_times.csv')

pit_stops =pd.read_csv('f1db_csv/pit_stops.csv')

qualifying =pd.read_csv('f1db_csv/qualifying.csv')

races =pd.read_csv('f1db_csv/races.csv', usecols = ['raceId','year','round','circuitId','name','date','time','url'])

results =pd.read_csv('f1db_csv/results.csv')

seasons =pd.read_csv('f1db_csv/seasons.csv')

sprint_results =pd.read_csv('f1db_csv/sprint_results.csv')

status =pd.read_csv('f1db_csv/status.csv')



# Visualizaçoes que vamos fazer
# por circuito:
#    volta mais rapida
#    average lap time over the years
#    pilotos com mais vitorias 
#    equipas com mais vitorias
#    pit stop mais rapido (equipa)
#    average pit stop time over the years
# por season
#    vencedor (equipa e piloto)
#    mais vitorias (equipa e piloto)
#    mais pole positions (equipa e piloto)
#    pit stop mais rapido (equipa)
# pilotos com mais vitorias e campeonatos
# equipas com mais vitorias e campeonatos
# por piloto
#
     

#DADOS
fullnames = drivers['forename'] + str(" ") + drivers['surname']
pilot_names = [dict(label=fullname, value=fullname) for fullname in fullnames]

encoded_image = base64.b64encode(open('images/avatar.png', 'rb').read())

#INTERACTIVE PARTS
    
#LAYOUT   
app = dash.Dash(__name__, assets_folder='style')

server = app.server

app.layout = html.Div([

       
    
       html.H1('F1 STATISTICS', id = 'title'), 
               
       html.Label('Drivers'),
       html.Br(),
       dcc.Dropdown(
        id='names_drop',
        options= pilot_names,
        value=[],
        multi=True,
        style={'backgroundColor': 'rgb(218,218,218)', 'color': 'black', 'font-size': '13px'}
    ),
       html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), id='avatar')
       
      
    
])







