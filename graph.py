
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
lines = pd.read_csv(r"D:/corona_data/covid-v-data.csv")
active_cases=lines.groupby(by="Entity").max()[['total_vaccinations_per_hundred','Day']].sort_values(by=["total_vaccinations_per_hundred"], ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10", size=50)
ax=sns.barplot(data=active_cases.iloc[:10],y="total_vaccinations_per_hundred",x="Entity", linewidth=2, edgecolor='red')
plt.show()