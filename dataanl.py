import numpy as np
import pandas as pd # data manipulation
# for data visualisation
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
from plotly.subplots import make_subplots
# for time
from datetime import datetime,date,time,timezone
import folium
df=pd.read_csv("D:/corona_data/covid-v-data.csv")
df['Date'] = pd.to_datetime(df['Day']) #convert string Date time into Python Date time object
df.set_index('Date',inplace=True) 
df.drop(['Day'],axis=1,inplace=True) #убирает данный столбец из данных
# print(df.head())
map_osm=folium.Map(location = [43.17638980564814, 76.93068214581893],
zoom_start=13,
tiles="stamenwatercolor",
)
folium.Marker(
   location= [43.17638980564814, 76.93068214581893],
    popup="Your location",
    icon=folium.Icon(icon="cloud"),
).add_to(map_osm)
folium.Marker(
   location= [43.17707032518363, 76.82674114506969], 
   popup="TimberLine Lodge", 
   icon=folium.Icon(color="green"),
).add_to(map_osm)
folium.CircleMarker(
    location=[43.17638980564814, 76.93068214581893],
    radius=100,
    popup="circle",
    color='#3186cc',
    fill=True,
    fill_color='#3186cc',
).add_to(map_osm)
map_osm.save('new.html')
