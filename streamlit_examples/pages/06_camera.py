import streamlit as st

enable = st.checkbox("Activar cámara")
picture = st.camera_input("Tomar foto", disabled=not enable)

if picture:
    st.image(picture)