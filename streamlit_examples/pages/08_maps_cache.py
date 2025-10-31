import pandas as pd
import streamlit as st

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    return df


def filter_by_hour_range(df, hour_min, hour_max):
    return df[(df['Date/Time'].dt.hour>=hour_min) & (df['Date/Time'].dt.hour<=hour_max)]



x = st.slider('Establece un range de Horario', 1, 24, (11,12))

st.session_state['range'] = x

url = "https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv"
df = load_data(url)
df = df.rename(columns={'Lat': 'lat', 'Lon': 'lon'})

df = filter_by_hour_range(df, x[0], x[1])
st.map(df)
