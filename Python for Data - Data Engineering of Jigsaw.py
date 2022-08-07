#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Specifying taxi trips near Madison Square Garden with the pulocationid (pickup location id)

# Selecting two of the trips near Madison Square Garden

import pandas as pd
url = "https://data.cityofnewyork.us/resource/biws-g3hs.json?pulocationid=186"
df = pd.read_json(url)
df[:2]


# In[2]:


# Searching the Itunes API for Billie Eilish albums and limiting to the first returned result.

import pandas as pd 
url = "https://itunes.apple.com/search?term=billie+eilish&entity=album&limit=1"
df = pd.read_json(url)
df.to_dict("records")


# In[3]:


# Plotting the data

import plotly.graph_objects as go
scatter = go.Scatter(x = [1, 2, 3], y = [4, 5, 6])
fig = go.Figure(data = scatter)
fig


# In[4]:


# Example of plotting the data

import plotly.graph_objects as go
ages = [27, 34, 58, 75]
names = ["Jarrad", "Elsa", "Wendy", "Neson"]
scatter_trace = go.Scatter(x = ["Jarrad", "Elsa", "Wendy", "Neson"], y = [27, 34, 58, 75])
fig = go.Figure(scatter_trace)
fig


# In[5]:


import plotly.graph_objects as go
movies = ["Spider Man", "Sing"]
revenues = [2000000, 3000000]
scatter = go.Scatter(x= movies , y= revenues )
go.Figure(scatter)


# In[6]:


movies = [ 
    {'titles':"Thor", 'revenues':5000000, 'budgets':3000000}, 
    {'titles':"Minions", 'revenues':5200000, 'budgets':3700000}
]

for movie in movies:
    print(movie["titles"])
    print(movie["revenues"])


# In[7]:


adults = ["alex", "julia", "tommy", "zack"]
for adult in adults:
    print(adult)
    
print("alex".title())
print("julia".upper())
print("tommy".capitalize())


# In[8]:


# Representing the populations of cities

import plotly.graph_objects as go
cities_scatter = go.Scatter(y = [8175133, 3792621, 2695598], hovertext = ["New York[d]", "Los Angeles", "Chicago"])

go.Figure(data = cities_scatter)


# In[9]:


# The numbers represent the points of each player scores on average in a game

import plotly.graph_objects as go

players = ["James Harden", "Giannis", "Luka Doncic", "Lebron James"]
points = [48, 40, 39, 35]

scatter_players = go.Scatter(x = players, y = points, mode = "markers")
go.Figure(scatter_players)


# In[10]:


players = ['James Harden', 'Giannis', 'Luka Doncic', 'Lebron James']
mid_players = players[1:3]

points = [48, 40, 39, 35]
mid_points = points[1:3]

print(players)
print(mid_players)
print(mid_points)

scatter_mid = go.Scatter(x = mid_players, y = mid_points, mode = "markers")
go. Figure(scatter_mid)


# In[11]:


# Looping through nested data

classmates = [ 
    {'name': "Evon", 'age': 24, 'weight': 65, 'education': "graduate diploma"}, 
    {'name': "Jessica", 'age': 21, 'weight': 50, 'education': "bachelor honours"}, 
    {'name': "Nick", 'age': 27, 'weight': 62, 'education': "master"},
    {'name': "Hellen", 'age': 28, 'weight': 52, 'education': "PhD"}
]

for classmate in classmates:
    print(classmate["education"])
    print(classmate["age"])


# In[ ]:


# Python Dictionaries

