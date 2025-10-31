import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(1).standard_normal((20, 3)), columns=["a", "b", "c"])

st.write(df)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.scatter_chart(df)