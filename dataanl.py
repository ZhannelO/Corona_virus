import numpy as np
import pandas as pd # data manipulation
# for data visualisation
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
from plotly.subplots import make_subplots
# for time
from datetime import datetime,date,time,timezone
df=pd.read_csv("D:/corona_data/covid-v-data.csv")
df['Date'] = pd.to_datetime(df['Day']) #convert string Date time into Python Date time object
df.set_index('Date',inplace=True) 
df.drop(['Day'],axis=1,inplace=True) #убирает данный столбец из данных
# print(df.head())
print(len(df['Entity'].unique()))
