import streamlit as st
import pandas as pd
import plotly_express as px

# Lectura de los datos
car_data = pd.read_csv('vehicles_us.csv')
# Título de la app
st.header('App Sprint 5 \"Visualización de datos\"')
# Creación casillas de verificación para el tipo de gráfico
build_histogram = st.checkbox('Construir un histograma')
build_dispersion = st.checkbox('Construir un diagrama de dispersión')
build_box = st.checkbox('Construir un diagrama de caja')
# Creación de un botón
hist_button = st.button('Construir gráfico')


if hist_button:  # acciones al hacer clic en el botón

    if build_histogram:
        # Mensaje a mostrar
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de autos')

        # Creación del histograma
        fig = px.histogram(car_data, x="odometer")

        # Muestra el histograma usando Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

    if build_dispersion:
        # Mensaje a mostrar
        st.write(
            'Creación de un diagrama de dispersión de odometer vs prices para el conjunto de datos de anuncios de venta de autos')

        # Creación del histograma
        fig = px.scatter(car_data, x="odometer", y="price")

        # Muestra el histograma usando Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

    if build_box:
        # Mensaje a mostrar
        st.write(
            'Creación de un diagrama de caja de price vs condition para el conjunto de datos de anuncios de venta de autos')

        # Creación del histograma
        fig = px.box(car_data, x="condition", y="price")

        # Muestra el histograma usando Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
