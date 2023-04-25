import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Pub Locations:round_pushpin:')
df = pd.read_csv('data\pubs.csv')
df = df.rename(columns={'latitude':'LAT','longtitude':'LON'})

fig = px.scatter_mapbox(df, lat="LAT", lon="LON", zoom=3)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

