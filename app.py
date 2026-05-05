import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de venta de coches en EE.UU.')

build_histogram = st.checkbox('Construir histograma de precios')

if build_histogram:
    st.write('Distribución de precios de los coches')
    fig = px.histogram(car_data, x='price', title='Distribución de precios')
    st.plotly_chart(fig)

build_scatter = st.checkbox('Construir gráfica de precio vs kilometraje')

if build_scatter:
    st.write('Relación entre precio y kilometraje')
    fig2 = px.scatter(car_data, x='odometer', y='price', title='Precio vs Kilometraje')
    st.plotly_chart(fig2)
        