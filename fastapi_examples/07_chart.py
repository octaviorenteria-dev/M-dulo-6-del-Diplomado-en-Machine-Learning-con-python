import pandas as pd
import streamlit as st
import requests
import time

chart_placeholder = st.empty()
data = None

while True:
    newdata = requests.get('http://127.0.0.1:8080/get/').json()
    if type(newdata) is list:
        newdata = pd.DataFrame(newdata)
        data = pd.concat([data,newdata],axis=0)
        with chart_placeholder.container():
            st.line_chart(data,x='timestamp',y='value')
    time.sleep(1)