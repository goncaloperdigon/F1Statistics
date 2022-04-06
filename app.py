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
pilot_names = [dict(label=fullname, value=driver_id) for fullname, driver_id in zip(fullnames, drivers['driverId'])]

encoded_image_avatar = base64.b64encode(open('images/avatar.png', 'rb').read())
encoded_image_logo = base64.b64encode(open('images/f1_logo.png', 'rb').read())


#INTERACTIVE PARTS
    
#LAYOUT   
app = dash.Dash(__name__, assets_folder='style')

server = app.server

app.layout = html.Div([

       html.Div([

           html.Img(src='data:image/png;base64,{}'.format(encoded_image_logo.decode()), id='logo'),

           html.H1('STATISTICS', id = 'title'),

        ], id = 'div_title'),


        html.Div([

        html.H5('Choose your driver', id = 'drivers_title'),

       html.Br(),

       dcc.Dropdown(
        id='names_drop',
        options= pilot_names,
        value=1,
        multi=False
    ),
       html.Img(src='data:image/png;base64,{}'.format(encoded_image_avatar.decode()), id='avatar')
       
    ], id = 'left_column_drivers'),
    
    html.Div([

    dcc.Graph(
        id='driver_stats_graph',

    )

    ], id = 'right_column_drivers')
])

@app.callback(
    Output(component_id='driver_stats_graph', component_property='figure'),
    [Input(component_id='names_drop', component_property='value')]
)
def update_driver_info(driver):

    fig = go.Figure(go.Bar(
        x=[len(qualifying.loc[(qualifying['position'] == 1) & (qualifying['driverId'] == driver)]),
           len(results.loc[(results['position'] == '1') & (results['driverId'] == driver)]),
           len(results.loc[results['driverId'] == driver])],
        y=[ 'Total Pole Postions','Total Wins', 'Total Number of Races'],
        marker=dict(
            color='rgba(222, 83, 83, 0.8)',
            line=dict(color='rgba(138, 8, 8, 0.8)', width=3)),
        orientation='h'))

    fig.layout.plot_bgcolor = 'rgb(30,30,30)'
    fig.layout.paper_bgcolor = 'rgb(30,30,30)'

    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            zeroline=False,
            range=[0, 400],
            tickfont=dict(
                family='Arial',
                size=13,
                color='white',
            ),

        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            zeroline=False,
            tickfont=dict(
                family='Arial',
                size=18,
                color='white',
            ),
        ),
        margin=dict(
            pad=20
        ),
        showlegend=False,
    )

    return go.Figure(data=fig)


if __name__ == '__main__':
    app.run_server(debug=True)





