import streamlit as st

x = st.slider('Elige un número', 0, 30, 10) #min, max, default

st.write(f"El valor del slider es :green-badge[{x}]")

pressed = st.button('botón')
if pressed:
    st.write(":green-badge[botón presionado]")


option = st.selectbox(
"¿Cómo prefiere que nos pongamos en contacto con usted?",
("Correo electrónico", "Teléfono fijo", "Teléfono móvil"),
)


st.write(f"Elemento seleccionado :green-badge[{option}]")


color = st.color_picker('Elige un color', '#000000')
st.write(f"Color seleccionado :green-badge[{color}]")

user_input = st.text_input("Escriba su nombre:")
if user_input:
    st.write(f'Hola: :green-badge[{user_input}]')