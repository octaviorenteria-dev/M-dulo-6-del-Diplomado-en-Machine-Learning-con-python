import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [100, 100] + [21.014, -101.254],
    columns=["lat", "lon"],
)

st.map(df)
st.write(df)