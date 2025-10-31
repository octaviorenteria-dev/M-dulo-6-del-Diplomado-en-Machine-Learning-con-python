import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

np.random.seed(1) # Para que los datos random siempre sean los mismos

N = 50  # numero de puntos
x = np.random.rand(N) # coordenadas en X
y = np.random.rand(N) # coordenadas en X
colors = np.random.rand(N) # colores
area = (30 * np.random.rand(N))**2 

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, s=area, c=colors, alpha=0.5)
st.pyplot(fig)
