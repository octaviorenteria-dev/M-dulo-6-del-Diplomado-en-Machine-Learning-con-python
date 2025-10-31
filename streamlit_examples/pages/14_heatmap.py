import pandas as pd
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    
    return df

@st.cache_data
def preprocess(df):
    df['pos'] = df.apply(lambda x:F"{x['Lat']},{x['Lon']}",axis=1)
    values = df.groupby('pos').count().reset_index().sort_values('Date/Time')
    values = values[['pos','Date/Time']].rename(columns={'Date/Time': 'deliveries'})

    values['lat']=values.apply(lambda x:float(x['pos'].split(',')[0]),axis=1)
    values['lon']=values.apply(lambda x:float(x['pos'].split(',')[1]),axis=1)
    return values

def get_center(df):
    return [df['lat'].mean(),df['lon'].mean()]

url = "https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv"
df = load_data(url)
df = preprocess(df)

center = get_center(df)

st.title("Data loading and cache")
st.subheader("uber-rides-data1.csv")

with st.expander("See source code"):
    with st.echo():
        
        m = leafmap.Map(center=center, zoom=8)
        m.add_heatmap(
            df,
            latitude="lat",
            longitude="lon",
            value="deliveries",
            #name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)