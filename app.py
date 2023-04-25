import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Pub Finder:beer:')

st.text_area("""
            Introducing "PubFinder'," the ultimate app for pub enthusiasts! 
            With just a few taps, you can discover the nearest five pubs in your area. 
            Say goodbye to wandering around aimlessly trying to find the perfect spot for a pint
            let PubFinder do the work for you! 
            """)
df = pd.read_csv('data\pubs.csv')
st.write("Basic information and statistics about the dataset.")
st.dataframe(df)
st.subheader('No. of Pubs = 35809')
st.subheader('No. of Postcodes = 45231')
st.subheader('No. of Null values')
st.write(df.isnull().sum())







            



