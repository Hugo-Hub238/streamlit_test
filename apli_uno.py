import streamlit as st
import pandas as pd
import plotly.express as px

# --- Cargar datos ---
df = pd.read_csv('vehicles_us.xlsx')

# --- Encabezado de la app ---
st.header('Análisis de Vehículos en EE.UU.')
st.write('Explora la distribución de los datos del conjunto de vehículos.')

# --- Mostrar tabla opcional ---
st.subheader('Vista del dataset')
st.dataframe(df.head())

# --- Botón para histograma de odómetro ---
if st.button('Construir histograma de odómetro'):
    st.write('Histograma de kilometraje (odómetro) de los vehículos')
    fig = px.histogram(df, x='odometer', title='Distribución del Odómetro')
    st.plotly_chart(fig)

# --- Botón para histograma de precio ---
if st.button('Construir histograma de precio'):
    st.write('Histograma de precios de los vehículos')
    fig = px.histogram(df, x='price', title='Distribución de Precios')
    st.plotly_chart(fig)

