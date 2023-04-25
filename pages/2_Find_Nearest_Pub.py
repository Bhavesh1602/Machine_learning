import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

st.title('Welcome to Find the Nearest Pub Page')
df = pd.read_csv('data\pubs.csv')
df = df.rename(columns={'latitude':'LAT','longtitude':'LON'})

lat = st.number_input('Enter latitude',format="%.6f")
lon = st.number_input('Enter longitude',format="%.6f")

button_click = st.button("Display Pubs")
if button_click == True:
        if lat != 0.00 and lon!= 0.00:
            arr_lat = np.array(df['LAT'])
            arr_lon = np.array(df['LON'])
            arr = np.vstack((arr_lat, arr_lon)).T
            ar = np.sqrt(np.sum((arr - (lat, lon)) ** 2, axis=1))
            ar = ar.reshape(-1, 1)
            res = np.hstack([arr, ar])
            d = pd.DataFrame(res, columns=['lat', 'lon', 'dict'])
            k = np.sort(res[:, [2]].ravel())[1:6]
            l = list(k)
            lat1 = []
            lon1 = []
            for i in l:
                f = d.loc[d['dict'] == i]
                lat1.append(float(f['lat'].values))
                lon1.append(float(f['lon'].values))

            df1 = pd.DataFrame({'lat': lat1, 'lon': lon1}, dtype='float64')
            st.map(df1)

        else:
            st.write("Enter lat,lon values again")
