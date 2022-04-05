#!/usr/bin/env python
# coding: utf-8



import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd
import numpy as np


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


# ### Circuits

# In[4]:


circuits.head()


# ### Constructor results

# In[5]:


constructor_results.head()


# ### Contrusctor standings

# In[6]:


constructor_standings.head()


# ### Constructors

# In[7]:


constructors.head()


# ### Driver standings

# In[8]:


driver_standings.head()


# ### Drivers

# In[9]:


drivers.head()


# ### Lap times

# In[10]:


lap_times.head()


# ### Pit Stops

# In[11]:


pit_stops.head()


# ### Qualifying

# In[12]:


qualifying.head()


# ### Races

# In[13]:


races.head()


# ### Results

# In[14]:


results.head()


# ### Seasons

# In[15]:


seasons.head()


# ### Sprint results

# In[16]:


sprint_results.head()


# ### Status

# In[17]:


status.head()


# In[18]:


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
# 
     

#DADOS    
pilot_names = [dict(label=surname, value=surname) for surname in drivers['surname'].unique()]

dropdown_names = dcc.Dropdown(
        id='names_drop',
        options=pilot_names,
        value=['Portugal'],
        multi=True
    )
    
    
app = dash.Dash(__name__, assets_folder='style')

server = app.server

app.layout = html.Div([

   html.Label('bjabsjas'),
    dropdown_names
])


@app.callback(
    [
        Input("names_drop", "value"),
       
    ]
)




