import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    return df

st.title("Data loading and cache")
st.subheader("uber-rides-data1.csv")

url = "https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv"

df = load_data(url)
st.write(df)