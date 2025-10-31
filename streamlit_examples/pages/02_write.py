import streamlit as st
import pandas as pd

df = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})

df # Esto mostrará el DataFrame en la app.

st.write(df)



