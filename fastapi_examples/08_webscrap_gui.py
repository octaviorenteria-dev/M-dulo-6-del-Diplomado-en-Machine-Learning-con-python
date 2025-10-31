import streamlit as st
import requests
import time

def set_state():    
    response = requests.get(f'http://127.0.0.1:8080/put/{st.session_state.page_selector}')
    st.write(response.text)

st.selectbox(
        'Pick a page to scrap',
        list(range(1,11)),
        key="page_selector",
        on_change=set_state
    )

placeholder = st.empty()

while True:
    data = requests.get('http://127.0.0.1:8080/get/').json()

    if type(data) is list:
        with placeholder.container():
            st.write(data)
        break
    time.sleep(1)