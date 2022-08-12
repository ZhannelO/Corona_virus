import numpy as np
import pandas as pd # data manipulation
import folium
import json
# for data visualisation
import matplotlib.pyplot as plt 
import seaborn as sns 
from datapackage import Package
import plotly.express as px
from plotly.subplots import make_subplots
# for time
from datetime import datetime,date,time,timezone
import folium
url=("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
state_geo=f"{url}/us-states.json"
state_unemployment=f'{url}/US_Unemployment_Oct2012.csv'
state_data=pd.read_csv(state_unemployment)
m=folium.Map(location=[48,-102],zoom_start=3)
folium.Choropleth(
	geo_data=state_geo,
	name="choropleth",
	data=state_data,
	columns=["State","Unemployment"],
	key_on='feauture.id',
	fill_color="YlGn",
	fill_opacity=0.7,
	line_opacity=0.2,
	legend_name="Unemployment Rate").add_to(m)
folium.LayerControl().add_to(m)
center=[43.18940800520172, 76.88810729096917]
m=folium.Map(location=center,zoom_start=2, max_bounds=True, min_zoom=1,min_lat=-84,max_lat=84,min_lon=-175,max_lon=187)
geo_path = Package('https://datahub.io/core/geo-countries/datapackage.json')
json_data=json.load(open(geo_path,))
folium.Choropleth(geo_data=json_data,data=total_df,columns=(total_df.index,'total_vacinatiobs_per_hundred'), key_on='propeties.COUNTRY',fill_color="RdYlGn",fill_opacity=0.7,line_opacity=0.5,).add_to(m)
Control().add_to(m)
df=pd.read_csv(r"C:\Users\Admin\Downloads\covid-v-data.csv")
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
